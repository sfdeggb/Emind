"""
EMIND 现代化聊天界面 - 与后端集成版本
"""

import gradio as gr
import json
import time
import os
import sys
from typing import List, Dict, Any
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from ..components.modern_components import ModernUIComponents, ModernChatInterface

# 导入后端逻辑
try:
    from emind.core.agent import MusicAgent
    from emind.core.config_manager import get_secure_config
    BACKEND_AVAILABLE = True
except ImportError:
    BACKEND_AVAILABLE = False
    print("警告: 后端模块不可用，将使用模拟响应")


class IntegratedChatInterface:
    """与后端集成的现代化聊天界面"""
    
    def __init__(self, config_path: str = "config/default.yaml"):
        self.messages = []
        self.current_emotion = "neutral"
        self.config_path = config_path
        self.agent = None
        
        # 初始化后端代理
        if BACKEND_AVAILABLE:
            try:
                self.agent = MusicAgent(config_path, mode="gradio")
                print("✅ 后端代理初始化成功")
            except Exception as e:
                print(f"❌ 后端代理初始化失败: {e}")
                self.agent = None
    
    def create_chat_ui(self):
        """创建与后端集成的聊天界面"""
        
        # 头部
        header = ModernUIComponents.create_header(
            title="💬 与EMIND对话",
            subtitle="描述您的音乐愿景，让AI为您创作"
        )
        
        # 情绪指示器
        emotion_indicator = ModernUIComponents.create_emotion_indicator(self.current_emotion)
        
        # 聊天界面
        with gr.Tab("💬 聊天", elem_id="chat_tab") as chat_tab:
            header
            emotion_indicator
            
            # 主要内容区域
            with gr.Row():
                with gr.Column(scale=3):
                    # 聊天历史
                    chat_history = gr.HTML(
                        value="<div style='text-align: center; padding: 2rem; color: var(--text-muted);'>开始与EMIND对话...</div>",
                        elem_id="chat_history"
                    )
                
                with gr.Column(scale=1):
                    # 快速操作
                    quick_actions_html = """
                    <div class="emind-card">
                        <h3 style="margin: 0 0 1rem 0; color: var(--text-primary); display: flex; align-items: center;">
                            <span style="margin-right: 0.5rem;">⚡</span>
                            快速操作
                        </h3>
                        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                            <button class="emind-btn" onclick="sendQuickMessage('创作一首欢快的流行歌曲')" style="font-size: 0.875rem; padding: 0.75rem 1rem;">
                                🎵 欢快流行歌曲
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('创作一首放松的轻音乐')" style="font-size: 0.875rem; padding: 0.75rem 1rem;">
                                🌊 放松轻音乐
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('创作一首激昂的摇滚歌曲')" style="font-size: 0.875rem; padding: 0.75rem 1rem;">
                                🎸 激昂摇滚歌曲
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('创作一首悲伤的抒情歌曲')" style="font-size: 0.875rem; padding: 0.75rem 1rem;">
                                💔 悲伤抒情歌曲
                            </button>
                        </div>
                    </div>
                    """
                    
                    gr.HTML(quick_actions_html)
                    
                    # 语音输入
                    voice_input = gr.Audio(
                        label="🎤 语音输入",
                        type="filepath",
                        elem_id="voice_input"
                    )
                    
                    # 设置面板
                    settings_panel = self.create_settings_panel()
            
            # 输入区域
            with gr.Row():
                with gr.Column(scale=4):
                    user_input = gr.Textbox(
                        placeholder="描述您想要创作的音乐... (例如：'一首关于夏天的欢快流行歌曲')",
                        label="",
                        lines=2,
                        elem_id="user_input",
                        show_label=False
                    )
                
                with gr.Column(scale=1):
                    send_button = gr.Button(
                        "发送",
                        variant="primary",
                        elem_id="send_button",
                        size="lg"
                    )
            
            # 状态和进度
            status_container = gr.HTML(
                value="<div id='status-container' style='display: none;'><div class='emind-loading' style='justify-content: center; padding: 1rem;'><div class='emind-spinner'></div><span style='margin-left: 0.5rem; color: var(--text-secondary);' id='status-text'>处理您的请求...</span></div></div>",
                elem_id="status_container"
            )
        
        # 事件处理函数
        def send_message(message: str, history: str) -> tuple:
            """发送消息并获取响应"""
            if not message.strip():
                return history, ""
            
            # 添加用户消息到历史
            user_message_html = ModernUIComponents.create_message_bubble(
                message, "user", time.strftime("%H:%M")
            )
            
            if history == "<div style='text-align: center; padding: 2rem; color: var(--text-muted);'>开始与EMIND对话...</div>":
                new_history = user_message_html
            else:
                new_history = history + user_message_html
            
            # 获取AI响应
            ai_response = self.get_ai_response(message)
            
            # 添加AI响应到历史
            ai_message_html = ModernUIComponents.create_message_bubble(
                ai_response, "assistant", time.strftime("%H:%M")
            )
            
            new_history += ai_message_html
            
            return new_history, ""
        
        def get_ai_response(self, message: str) -> str:
            """获取AI响应"""
            if self.agent and BACKEND_AVAILABLE:
                try:
                    # 使用真实的后端代理
                    response = self.agent.skillchat(message, self.agent.chatbot, self.agent.chat_context)
                    return response
                except Exception as e:
                    print(f"后端处理错误: {e}")
                    return f"抱歉，处理您的请求时出现错误: {str(e)}"
            else:
                # 使用模拟响应
                return self.get_mock_response(message)
        
        def get_mock_response(self, message: str) -> str:
            """获取模拟响应"""
            responses = [
                "我将为您创作这首音乐！让我开始生成一首美妙的曲目...",
                "很棒的想法！我正在处理您的请求，很快就会有令人惊叹的作品。",
                "完美！我理解您想要的内容。让我为您创作...",
                "优秀的选择！我正在根据您的描述生成音乐...",
                "我喜欢这个概念！让我为您创作一些特别的东西..."
            ]
            
            import random
            return random.choice(responses)
        
        def process_voice_input(audio_path: str) -> str:
            """处理语音输入"""
            if audio_path:
                # 这里可以集成语音转文字功能
                return "我听到了您的语音输入。让我为您处理..."
            return ""
        
        # 连接事件处理器
        send_button.click(
            send_message,
            inputs=[user_input, chat_history],
            outputs=[chat_history, user_input]
        )
        
        user_input.submit(
            send_message,
            inputs=[user_input, chat_history],
            outputs=[chat_history, user_input]
        )
        
        voice_input.change(
            process_voice_input,
            inputs=[voice_input],
            outputs=[user_input]
        )
        
        # JavaScript代码
        js_code = """
        <script>
            function sendQuickMessage(message) {
                const input = document.getElementById('user_input');
                const sendBtn = document.getElementById('send_button');
                
                if (input) {
                    input.value = message;
                    sendBtn.click();
                }
            }
            
            // 自动调整文本框高度
            const textarea = document.getElementById('user_input');
            if (textarea) {
                textarea.addEventListener('input', function() {
                    this.style.height = 'auto';
                    this.style.height = this.scrollHeight + 'px';
                });
            }
            
            // 显示/隐藏状态
            function showStatus(text) {
                const statusContainer = document.getElementById('status-container');
                const statusText = document.getElementById('status-text');
                
                if (statusContainer && statusText) {
                    statusText.textContent = text;
                    statusContainer.style.display = 'block';
                }
            }
            
            function hideStatus() {
                const statusContainer = document.getElementById('status-container');
                if (statusContainer) {
                    statusContainer.style.display = 'none';
                }
            }
            
            // 聊天历史自动滚动到底部
            function scrollToBottom() {
                const chatHistory = document.getElementById('chat_history');
                if (chatHistory) {
                    chatHistory.scrollTop = chatHistory.scrollHeight;
                }
            }
            
            // 监听新消息
            const observer = new MutationObserver(function(mutations) {
                mutations.forEach(function(mutation) {
                    if (mutation.type === 'childList') {
                        scrollToBottom();
                    }
                });
            });
            
            document.addEventListener('DOMContentLoaded', function() {
                const chatHistory = document.getElementById('chat_history');
                if (chatHistory) {
                    observer.observe(chatHistory, { childList: true, subtree: true });
                }
            });
            
            // 键盘快捷键
            document.addEventListener('keydown', function(e) {
                if (e.ctrlKey && e.key === 'Enter') {
                    const sendBtn = document.getElementById('send_button');
                    if (sendBtn) {
                        sendBtn.click();
                    }
                }
            });
        </script>
        """
        
        gr.HTML(js_code)
        
        return chat_tab
    
    def create_settings_panel(self) -> gr.HTML:
        """创建设置面板"""
        settings_html = """
        <div class="emind-card">
            <h3 style="margin: 0 0 1rem 0; color: var(--text-primary); display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">⚙️</span>
                设置
            </h3>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500;">音乐风格</label>
                    <select class="emind-input" style="padding: 0.5rem;">
                        <option>自动检测</option>
                        <option>流行</option>
                        <option>摇滚</option>
                        <option>古典</option>
                        <option>爵士</option>
                        <option>电子</option>
                    </select>
                </div>
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500;">时长</label>
                    <select class="emind-input" style="padding: 0.5rem;">
                        <option>30秒</option>
                        <option>1分钟</option>
                        <option>2分钟</option>
                        <option>3分钟</option>
                    </select>
                </div>
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500;">质量</label>
                    <select class="emind-input" style="padding: 0.5rem;">
                        <option>标准</option>
                        <option>高质量</option>
                        <option>超高质量</option>
                    </select>
                </div>
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem; font-weight: 500;">情绪</label>
                    <select class="emind-input" style="padding: 0.5rem;">
                        <option>自动检测</option>
                        <option>快乐</option>
                        <option>悲伤</option>
                        <option>兴奋</option>
                        <option>平静</option>
                        <option>愤怒</option>
                    </select>
                </div>
            </div>
        </div>
        """
        return gr.HTML(settings_html)


def create_integrated_chat_demo():
    """创建集成聊天界面演示"""
    chat_interface = IntegratedChatInterface()
    
    with gr.Blocks(
        title="EMIND - 集成聊天界面",
        ,
        theme=gr.themes.Soft()
    ) as demo:
        chat_interface.create_chat_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_integrated_chat_demo()
    demo.launch(server_name="0.0.0.0", server_port=8026)
