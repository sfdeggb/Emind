"""
EMIND 现代化UI组件系统 - 中文界面
"""

import gradio as gr
from typing import Optional, List, Dict, Any
import json
import time


class ModernUIComponents:
    """现代化UI组件库"""
    
    @staticmethod
    def create_header(title: str = "🎧 EMIND", subtitle: str = "您的AI音乐创作伙伴") -> gr.HTML:
        """创建现代化头部组件"""
        header_html = f"""
        <div class="emind-header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """
        return gr.HTML(header_html)
    
    @staticmethod
    def create_feature_card(title: str, description: str, icon: str = "🎵") -> gr.HTML:
        """创建功能卡片组件"""
        card_html = f"""
        <div class="emind-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 2.5rem; margin-right: 1rem;">{icon}</span>
                <h3 style="margin: 0; color: var(--text-primary); font-size: 1.25rem;">{title}</h3>
            </div>
            <p style="margin: 0; color: var(--text-secondary); line-height: 1.6; font-size: 0.95rem;">{description}</p>
        </div>
        """
        return gr.HTML(card_html)
    
    @staticmethod
    def create_audio_player(audio_path: str, title: str = "生成的音频") -> gr.HTML:
        """创建现代化音频播放器组件"""
        player_html = f"""
        <div class="emind-audio-player">
            <h4 style="margin: 0 0 1rem 0; color: var(--text-primary); display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🎵</span>
                {title}
            </h4>
            <audio controls style="width: 100%; border-radius: var(--radius-xl); margin-bottom: 1rem;">
                <source src="{audio_path}" type="audio/mpeg">
                您的浏览器不支持音频播放。
            </audio>
            <div class="emind-audio-controls">
                <button class="emind-play-btn" onclick="togglePlay()">
                    <span id="play-icon">▶</span>
                </button>
                <div class="emind-progress" style="flex: 1;">
                    <div class="emind-progress-bar" id="progress-bar" style="width: 0%;"></div>
                </div>
                <span id="time-display" style="color: var(--text-secondary); font-size: 0.875rem; min-width: 80px;">0:00 / 0:00</span>
            </div>
        </div>
        <script>
            let isPlaying = false;
            const audio = document.querySelector('audio');
            const playBtn = document.querySelector('.emind-play-btn');
            const playIcon = document.getElementById('play-icon');
            const progressBar = document.getElementById('progress-bar');
            const timeDisplay = document.getElementById('time-display');
            
            function togglePlay() {{
                if (isPlaying) {{
                    audio.pause();
                    playIcon.textContent = '▶';
                    isPlaying = false;
                }} else {{
                    audio.play();
                    playIcon.textContent = '⏸';
                    isPlaying = true;
                }}
            }}
            
            audio.addEventListener('timeupdate', function() {{
                const progress = (audio.currentTime / audio.duration) * 100;
                progressBar.style.width = progress + '%';
                
                const currentTime = formatTime(audio.currentTime);
                const duration = formatTime(audio.duration);
                timeDisplay.textContent = currentTime + ' / ' + duration;
            }});
            
            function formatTime(seconds) {{
                const mins = Math.floor(seconds / 60);
                const secs = Math.floor(seconds % 60);
                return mins + ':' + (secs < 10 ? '0' : '') + secs;
            }}
        </script>
        """
        return gr.HTML(player_html)
    
    @staticmethod
    def create_loading_spinner(text: str = "处理中...") -> gr.HTML:
        """创建加载动画组件"""
        spinner_html = f"""
        <div class="emind-loading" style="justify-content: center; padding: 2rem;">
            <div class="emind-spinner"></div>
            <span style="margin-left: 0.5rem; color: var(--text-secondary); font-weight: 500;">{text}</span>
        </div>
        """
        return gr.HTML(spinner_html)
    
    @staticmethod
    def create_progress_bar(progress: float = 0.0, text: str = "") -> gr.HTML:
        """创建进度条组件"""
        progress_html = f"""
        <div style="margin: 1rem 0;">
            <div class="emind-progress">
                <div class="emind-progress-bar" style="width: {progress * 100}%;"></div>
            </div>
            {f'<p style="text-align: center; margin: 0.5rem 0; color: var(--text-secondary); font-weight: 500;">{text}</p>' if text else ''}
        </div>
        """
        return gr.HTML(progress_html)
    
    @staticmethod
    def create_message_bubble(message: str, sender: str = "assistant", timestamp: str = "") -> gr.HTML:
        """创建消息气泡组件"""
        sender_class = sender.lower()
        time_html = f'<small style="opacity: 0.7; font-size: 0.75rem; color: var(--text-muted);">{timestamp}</small>' if timestamp else ''
        
        # 根据发送者类型设置不同的样式
        if sender_class == "user":
            icon = "👤"
            sender_name = "您"
        elif sender_class == "assistant":
            icon = "🤖"
            sender_name = "EMIND"
        else:
            icon = "ℹ️"
            sender_name = "系统"
        
        bubble_html = f"""
        <div class="emind-message {sender_class}">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="margin-right: 0.5rem; font-size: 1.2rem;">{icon}</span>
                <strong style="font-size: 0.875rem; opacity: 0.8;">{sender_name}</strong>
                {time_html}
            </div>
            <div style="margin-bottom: 0.5rem;">{message}</div>
        </div>
        """
        return gr.HTML(bubble_html)
    
    @staticmethod
    def create_feature_grid(features: List[Dict[str, str]]) -> gr.HTML:
        """创建功能网格组件"""
        cards_html = ""
        for feature in features:
            title = feature.get('title', '')
            description = feature.get('description', '')
            icon = feature.get('icon', '🎵')
            cards_html += f"""
            <div class="emind-card" style="margin-bottom: 1.5rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 2.5rem; margin-right: 1rem;">{icon}</span>
                    <h3 style="margin: 0; color: var(--text-primary); font-size: 1.25rem;">{title}</h3>
                </div>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.6; font-size: 0.95rem;">{description}</p>
            </div>
            """
        
        grid_html = f"""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
            {cards_html}
        </div>
        """
        return gr.HTML(grid_html)
    
    @staticmethod
    def create_theme_toggle() -> gr.HTML:
        """创建主题切换按钮"""
        toggle_html = """
        <div class="theme-toggle" onclick="toggleTheme()" id="theme-toggle">
            <span id="theme-icon">🌙</span>
        </div>
        <script>
            function toggleTheme() {
                const body = document.body;
                const currentTheme = body.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                const themeIcon = document.getElementById('theme-icon');
                
                body.setAttribute('data-theme', newTheme);
                themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
                
                // 保存主题偏好
                localStorage.setItem('emind-theme', newTheme);
                
                // 显示切换通知
                showNotification(`已切换到${newTheme === 'dark' ? '深色' : '浅色'}主题`, 'success');
            }
            
            // 加载保存的主题
            document.addEventListener('DOMContentLoaded', function() {
                const savedTheme = localStorage.getItem('emind-theme') || 'light';
                document.body.setAttribute('data-theme', savedTheme);
                document.getElementById('theme-icon').textContent = savedTheme === 'dark' ? '☀️' : '🌙';
            });
        </script>
        """
        return gr.HTML(toggle_html)
    
    @staticmethod
    def create_stats_dashboard(stats: Dict[str, Any]) -> gr.HTML:
        """创建统计仪表板组件"""
        stats_html = ""
        for key, value in stats.items():
            stats_html += f"""
            <div class="emind-card" style="text-align: center; padding: 1.5rem;">
                <h2 style="margin: 0; color: var(--primary-color); font-size: 2.5rem; font-weight: 800;">{value}</h2>
                <p style="margin: 0.5rem 0 0 0; color: var(--text-secondary); text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em; font-weight: 600;">{key}</p>
            </div>
            """
        
        dashboard_html = f"""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
            {stats_html}
        </div>
        """
        return gr.HTML(dashboard_html)
    
    @staticmethod
    def create_notification(message: str, type: str = "info") -> gr.HTML:
        """创建通知组件"""
        type_colors = {
            "info": "var(--info-color)",
            "success": "var(--success-color)",
            "warning": "var(--warning-color)",
            "error": "var(--error-color)"
        }
        
        type_icons = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "❌"
        }
        
        color = type_colors.get(type, "var(--info-color)")
        icon = type_icons.get(type, "ℹ️")
        
        notification_html = f"""
        <div class="emind-notification {type}" style="border-left-color: {color};">
            <div style="display: flex; align-items: center;">
                <span style="margin-right: 0.5rem; font-size: 1.2rem;">{icon}</span>
                <p style="margin: 0; color: var(--text-primary); font-weight: 500;">{message}</p>
            </div>
        </div>
        """
        return gr.HTML(notification_html)
    
    @staticmethod
    def create_quick_action_button(text: str, icon: str = "🎵", onclick: str = "") -> gr.HTML:
        """创建快速操作按钮"""
        button_html = f"""
        <button class="emind-btn" onclick="{onclick}" style="width: 100%; margin-bottom: 0.5rem; font-size: 0.875rem; padding: 0.75rem 1rem;">
            <span style="margin-right: 0.5rem;">{icon}</span>
            {text}
        </button>
        """
        return gr.HTML(button_html)
    
    @staticmethod
    def create_emotion_indicator(emotion: str = "neutral") -> gr.HTML:
        """创建情绪指示器"""
        emotion_icons = {
            "happy": "😊",
            "sad": "😢",
            "angry": "😠",
            "excited": "🤩",
            "calm": "😌",
            "neutral": "😐"
        }
        
        emotion_colors = {
            "happy": "var(--success-color)",
            "sad": "var(--info-color)",
            "angry": "var(--error-color)",
            "excited": "var(--warning-color)",
            "calm": "var(--accent-color)",
            "neutral": "var(--text-muted)"
        }
        
        icon = emotion_icons.get(emotion, "😐")
        color = emotion_colors.get(emotion, "var(--text-muted)")
        
        indicator_html = f"""
        <div class="emind-card" style="text-align: center; padding: 1rem;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
                <span style="font-size: 2rem;">{icon}</span>
                <div>
                    <h4 style="margin: 0; color: var(--text-primary);">当前情绪</h4>
                    <p style="margin: 0; color: {color}; font-weight: 600;" id="emotion-display">{emotion.title()}</p>
                </div>
            </div>
        </div>
        """
        return gr.HTML(indicator_html)


class ModernLayout:
    """现代化布局工具"""
    
    @staticmethod
    def create_sidebar_layout(sidebar_content: List[Any], main_content: List[Any]) -> gr.Blocks:
        """创建侧边栏布局"""
        with gr.Blocks(css_file="emind/ui/web/components/styles/modern_theme.css") as layout:
            with gr.Row():
                with gr.Column(scale=1):
                    gr.HTML('<div style="padding: 1rem;">')
                    for content in sidebar_content:
                        content
                    gr.HTML('</div>')
                
                with gr.Column(scale=3):
                    for content in main_content:
                        content
        
        return layout
    
    @staticmethod
    def create_centered_layout(content: List[Any], max_width: str = "1200px") -> gr.Blocks:
        """创建居中布局"""
        with gr.Blocks(css_file="emind/ui/web/components/styles/modern_theme.css") as layout:
            gr.HTML(f'<div style="max-width: {max_width}; margin: 0 auto; padding: 2rem;">')
            for item in content:
                item
            gr.HTML('</div>')
        
        return layout
    
    @staticmethod
    def create_tabbed_layout(tabs: Dict[str, List[Any]]) -> gr.Blocks:
        """创建标签页布局"""
        with gr.Blocks(css_file="emind/ui/web/components/styles/modern_theme.css") as layout:
            with gr.Tabs():
                for tab_name, tab_content in tabs.items():
                    with gr.Tab(tab_name):
                        for content in tab_content:
                            content
        
        return layout


class ModernChatInterface:
    """现代化聊天界面"""
    
    def __init__(self):
        self.messages = []
        self.current_emotion = "neutral"
    
    def create_chat_input(self, placeholder: str = "描述您想要创作的音乐...") -> tuple:
        """创建聊天输入组件"""
        with gr.Row():
            with gr.Column(scale=4):
                user_input = gr.Textbox(
                    placeholder=placeholder,
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
        
        return user_input, send_button
    
    def create_voice_input(self) -> gr.Audio:
        """创建语音输入组件"""
        return gr.Audio(
            label="🎤 语音输入",
            type="filepath",
            elem_id="voice_input"
        )
    
    def create_chat_history(self) -> gr.HTML:
        """创建聊天历史组件"""
        return gr.HTML(
            value="<div style='text-align: center; padding: 2rem; color: var(--text-muted);'>开始与EMIND对话...</div>",
            elem_id="chat_history"
        )
    
    def create_quick_actions(self) -> gr.HTML:
        """创建快速操作组件"""
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
        return gr.HTML(quick_actions_html)
    
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
            </div>
        </div>
        """
        return gr.HTML(settings_html)
