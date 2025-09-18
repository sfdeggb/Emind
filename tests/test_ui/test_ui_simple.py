#!/usr/bin/env python3
"""
简化的UI测试脚本
"""

import gradio as gr
import os

def create_simple_modern_ui():
    """创建简化的现代UI测试"""
    
    # 简化的CSS样式
    css = """
    .emind-header {
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .emind-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 1rem;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .emind-btn {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .emind-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    """
    
    with gr.Blocks(css=css, title="🎧 EMIND - Modern UI Test") as demo:
        
        # 头部
        header_html = """
        <div class="emind-header">
            <h1>🎧 EMIND</h1>
            <p>Your AI Music Companion - Modern UI Test</p>
        </div>
        """
        gr.HTML(header_html)
        
        # 功能卡片
        with gr.Row():
            with gr.Column():
                card1_html = """
                <div class="emind-card">
                    <h3>🎵 AI Music Generation</h3>
                    <p>Generate original music from text descriptions using advanced AI models.</p>
                </div>
                """
                gr.HTML(card1_html)
            
            with gr.Column():
                card2_html = """
                <div class="emind-card">
                    <h3>😊 Emotion Analysis</h3>
                    <p>Analyze your mood and generate music that matches your emotional state.</p>
                </div>
                """
                gr.HTML(card2_html)
        
        # 聊天界面
        with gr.Row():
            with gr.Column(scale=3):
                chatbot = gr.Chatbot(label="Chat with EMIND", height=400)
                msg = gr.Textbox(label="Message", placeholder="Describe the music you want to create...")
                send_btn = gr.Button("Send", variant="primary")
            
            with gr.Column(scale=1):
                # 快速操作
                quick_actions_html = """
                <div class="emind-card">
                    <h3>Quick Actions</h3>
                    <button class="emind-btn" onclick="sendQuickMessage('Generate a happy pop song')">
                        🎵 Happy Pop Song
                    </button>
                    <br><br>
                    <button class="emind-btn" onclick="sendQuickMessage('Create a relaxing ambient track')">
                        🌊 Relaxing Ambient
                    </button>
                    <br><br>
                    <button class="emind-btn" onclick="sendQuickMessage('Make an energetic rock anthem')">
                        🎸 Rock Anthem
                    </button>
                </div>
                """
                gr.HTML(quick_actions_html)
        
        # 设置面板
        with gr.Accordion("⚙️ Settings", open=False):
            with gr.Row():
                with gr.Column():
                    gr.Dropdown(["GPT-3.5", "GPT-4", "Claude-3"], label="AI Model", value="GPT-3.5")
                    gr.Dropdown(["30s", "1min", "2min", "3min"], label="Duration", value="1min")
                with gr.Column():
                    gr.Dropdown(["Standard", "High", "Ultra"], label="Quality", value="High")
                    gr.Checkbox(label="Use GPU", value=True)
        
        # 事件处理
        def respond(message, history):
            if not message.strip():
                return history, ""
            
            # 模拟AI响应
            responses = [
                "I'll create that music for you! Let me work on generating a beautiful track...",
                "Great idea! I'm processing your request and will have something amazing for you soon.",
                "Perfect! I understand what you're looking for. Let me compose that for you...",
                "Excellent choice! I'm generating the music based on your description...",
                "I love that concept! Let me create something special for you..."
            ]
            
            import random
            response = random.choice(responses)
            
            history.append([message, response])
            return history, ""
        
        send_btn.click(respond, [msg, chatbot], [chatbot, msg])
        msg.submit(respond, [msg, chatbot], [chatbot, msg])
        
        # JavaScript
        js_code = """
        <script>
            function sendQuickMessage(message) {
                const input = document.querySelector('input[placeholder*="Describe"]');
                const sendBtn = document.querySelector('button[variant="primary"]');
                
                if (input && sendBtn) {
                    input.value = message;
                    sendBtn.click();
                }
            }
        </script>
        """
        gr.HTML(js_code)
    
    return demo

if __name__ == "__main__":
    print("🎧 Starting EMIND Modern UI Test...")
    demo = create_simple_modern_ui()
    demo.launch(server_name="0.0.0.0", server_port=8026, inbrowser=True)
