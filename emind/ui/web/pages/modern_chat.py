"""
Modern Chat Interface for Emind
"""

import gradio as gr
import json
import time
from typing import List, Dict, Any
from ..components.modern_components import ModernUIComponents


class ModernChatInterface:
    """Modern chat interface for Emind"""
    
    def __init__(self):
        self.messages = []
        self.current_emotion = "neutral"
    
    def create_chat_ui(self):
        """Create the modern chat interface"""
        
        # Header
        header = ModernUIComponents.create_header(
            title="💬 Chat with EMIND",
            subtitle="Describe your musical vision and let AI create it for you"
        )
        
        # Emotion indicator
        emotion_html = f"""
        <div class="emind-card" style="text-align: center; padding: 1rem;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
                <span style="font-size: 1.5rem;">😊</span>
                <div>
                    <h4 style="margin: 0; color: var(--text-primary);">Current Mood</h4>
                    <p style="margin: 0; color: var(--text-secondary);" id="emotion-display">Neutral</p>
                </div>
            </div>
        </div>
        """
        
        # Chat container
        with gr.Tab("💬 Chat", elem_id="chat_tab") as chat_tab:
            header
            gr.HTML(emotion_html)
            
            # Chat history
            with gr.Row():
                with gr.Column(scale=3):
                    chat_history = gr.HTML(
                        value="<div style='text-align: center; padding: 2rem; color: var(--text-muted);'>Start a conversation with EMIND...</div>",
                        elem_id="chat_history"
                    )
                
                with gr.Column(scale=1):
                    # Quick actions
                    quick_actions_html = """
                    <div class="emind-card">
                        <h3 style="margin: 0 0 1rem 0; color: var(--text-primary);">Quick Actions</h3>
                        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
                            <button class="emind-btn" onclick="sendQuickMessage('Generate a happy pop song')" style="font-size: 0.875rem; padding: 0.5rem 1rem;">
                                🎵 Happy Pop Song
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('Create a relaxing ambient track')" style="font-size: 0.875rem; padding: 0.5rem 1rem;">
                                🌊 Relaxing Ambient
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('Make a energetic rock anthem')" style="font-size: 0.875rem; padding: 0.5rem 1rem;">
                                🎸 Rock Anthem
                            </button>
                            <button class="emind-btn" onclick="sendQuickMessage('Generate a sad ballad')" style="font-size: 0.875rem; padding: 0.5rem 1rem;">
                                💔 Sad Ballad
                            </button>
                        </div>
                    </div>
                    """
                    
                    gr.HTML(quick_actions_html)
                    
                    # Voice input
                    voice_input = gr.Audio(
                        label="🎤 Voice Input",
                        type="filepath",
                        elem_id="voice_input"
                    )
                    
                    # Settings
                    settings_html = """
                    <div class="emind-card">
                        <h3 style="margin: 0 0 1rem 0; color: var(--text-primary);">Settings</h3>
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <div>
                                <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem;">Music Style</label>
                                <select class="emind-input" style="padding: 0.5rem;">
                                    <option>Auto-detect</option>
                                    <option>Pop</option>
                                    <option>Rock</option>
                                    <option>Classical</option>
                                    <option>Jazz</option>
                                    <option>Electronic</option>
                                </select>
                            </div>
                            <div>
                                <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem;">Duration</label>
                                <select class="emind-input" style="padding: 0.5rem;">
                                    <option>30 seconds</option>
                                    <option>1 minute</option>
                                    <option>2 minutes</option>
                                    <option>3 minutes</option>
                                </select>
                            </div>
                            <div>
                                <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-size: 0.875rem;">Quality</label>
                                <select class="emind-input" style="padding: 0.5rem;">
                                    <option>Standard</option>
                                    <option>High</option>
                                    <option>Ultra</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    """
                    
                    gr.HTML(settings_html)
            
            # Input area
            with gr.Row():
                with gr.Column(scale=4):
                    user_input = gr.Textbox(
                        placeholder="Describe the music you want to create... (e.g., 'A happy pop song about summer')",
                        label="",
                        lines=2,
                        elem_id="user_input"
                    )
                
                with gr.Column(scale=1):
                    send_button = gr.Button(
                        "Send",
                        variant="primary",
                        elem_id="send_button"
                    )
            
            # Status and progress
            status_html = """
            <div id="status-container" style="display: none;">
                <div class="emind-loading" style="justify-content: center; padding: 1rem;">
                    <div class="emind-spinner"></div>
                    <span style="margin-left: 0.5rem; color: var(--text-secondary);" id="status-text">Processing your request...</span>
                </div>
            </div>
            """
            
            gr.HTML(status_html)
        
        # Event handlers
        def send_message(message: str, history: str) -> tuple:
            """Send a message and get response"""
            if not message.strip():
                return history, ""
            
            # Add user message to history
            user_message_html = ModernUIComponents.create_message_bubble(
                message, "user", time.strftime("%H:%M")
            )
            
            if history == "<div style='text-align: center; padding: 2rem; color: var(--text-muted);'>Start a conversation with EMIND...</div>":
                new_history = user_message_html
            else:
                new_history = history + user_message_html
            
            # Simulate AI response (replace with actual AI call)
            ai_response = self.generate_ai_response(message)
            
            # Add AI response to history
            ai_message_html = ModernUIComponents.create_message_bubble(
                ai_response, "assistant", time.strftime("%H:%M")
            )
            
            new_history += ai_message_html
            
            return new_history, ""
        
        def generate_ai_response(message: str) -> str:
            """Generate AI response (placeholder)"""
            # This would be replaced with actual AI integration
            responses = [
                "I'll create that music for you! Let me work on generating a beautiful track...",
                "Great idea! I'm processing your request and will have something amazing for you soon.",
                "Perfect! I understand what you're looking for. Let me compose that for you...",
                "Excellent choice! I'm generating the music based on your description...",
                "I love that concept! Let me create something special for you..."
            ]
            
            import random
            return random.choice(responses)
        
        def process_voice_input(audio_path: str) -> str:
            """Process voice input (placeholder)"""
            if audio_path:
                # This would integrate with speech-to-text
                return "I heard your voice input. Let me process that for you..."
            return ""
        
        # Connect event handlers
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
        
        # JavaScript for quick actions
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
            
            // Auto-resize textarea
            const textarea = document.getElementById('user_input');
            if (textarea) {
                textarea.addEventListener('input', function() {
                    this.style.height = 'auto';
                    this.style.height = this.scrollHeight + 'px';
                });
            }
            
            // Show/hide status
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
        </script>
        """
        
        gr.HTML(js_code)
        
        return chat_tab


def create_modern_chat_demo():
    """Create a demo of the modern chat interface"""
    chat_interface = ModernChatInterface()
    
    with gr.Blocks(
        title="EMIND - Modern Chat",
        css_file="emind/ui/web/components/styles/modern_theme.css",
        theme=gr.themes.Soft()
    ) as demo:
        chat_interface.create_chat_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_modern_chat_demo()
    demo.launch(server_name="0.0.0.0", server_port=8024)
