"""
Modern Settings Page for Emind
"""

import gradio as gr
from ..components.modern_components import ModernUIComponents


def create_modern_settings_ui():
    """Create a modern settings page"""
    
    # Header
    header = ModernUIComponents.create_header(
        title="⚙️ Settings",
        subtitle="Customize your EMIND experience"
    )
    
    with gr.Tab("⚙️ Settings", elem_id="settings_tab") as settings_tab:
        header
        
        with gr.Row():
            with gr.Column(scale=2):
                # API Configuration
                api_config_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🔑</span>
                        API Configuration
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">OpenAI API Key</label>
                            <input type="password" class="emind-input" placeholder="sk-..." style="font-family: monospace;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">HuggingFace Token</label>
                            <input type="password" class="emind-input" placeholder="hf_..." style="font-family: monospace;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Spotify Client ID</label>
                            <input type="text" class="emind-input" placeholder="Your Spotify Client ID">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Google API Key</label>
                            <input type="password" class="emind-input" placeholder="AIza...">
                        </div>
                        <button class="emind-btn" style="align-self: flex-start;">
                            Save API Keys
                        </button>
                    </div>
                </div>
                """
                
                gr.HTML(api_config_html)
                
                # Model Settings
                model_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🤖</span>
                        Model Settings
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Default Model</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>GPT-3.5 Turbo</option>
                                <option>GPT-4</option>
                                <option>Claude-3</option>
                                <option>Local Model</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Music Generation Model</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>MUZIC (Recommended)</option>
                                <option>MusicLM</option>
                                <option>Jukebox</option>
                                <option>Custom Model</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Voice Synthesis Model</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>DiffSinger</option>
                                <option>Tacotron2</option>
                                <option>FastSpeech2</option>
                                <option>Custom TTS</option>
                            </select>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="use-gpu" style="transform: scale(1.2);">
                            <label for="use-gpu" style="color: var(--text-secondary); font-weight: 500;">Use GPU acceleration</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(model_settings_html)
            
            with gr.Column(scale=1):
                # Audio Settings
                audio_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🎵</span>
                        Audio Settings
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Sample Rate</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>44.1 kHz</option>
                                <option>48 kHz</option>
                                <option>96 kHz</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Bit Depth</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>16-bit</option>
                                <option>24-bit</option>
                                <option>32-bit</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Output Format</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>MP3</option>
                                <option>WAV</option>
                                <option>FLAC</option>
                                <option>OGG</option>
                            </select>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="auto-download" style="transform: scale(1.2);">
                            <label for="auto-download" style="color: var(--text-secondary); font-weight: 500;">Auto-download generated files</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(audio_settings_html)
                
                # Interface Settings
                interface_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🎨</span>
                        Interface Settings
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Theme</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>Light</option>
                                <option>Dark</option>
                                <option>Auto</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Language</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>English</option>
                                <option>中文</option>
                                <option>日本語</option>
                                <option>Español</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Font Size</label>
                            <input type="range" min="12" max="20" value="16" class="emind-input" style="padding: 0;">
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="animations" style="transform: scale(1.2);" checked>
                            <label for="animations" style="color: var(--text-secondary); font-weight: 500;">Enable animations</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="notifications" style="transform: scale(1.2);" checked>
                            <label for="notifications" style="color: var(--text-secondary); font-weight: 500;">Show notifications</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(interface_settings_html)
        
        # Advanced Settings
        advanced_settings_html = """
        <div class="emind-card">
            <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🔧</span>
                Advanced Settings
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">Performance</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Max Concurrent Requests</label>
                            <input type="number" class="emind-input" value="3" min="1" max="10">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Request Timeout (seconds)</label>
                            <input type="number" class="emind-input" value="30" min="5" max="300">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Cache Size (MB)</label>
                            <input type="number" class="emind-input" value="100" min="10" max="1000">
                        </div>
                    </div>
                </div>
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">Storage</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Output Directory</label>
                            <input type="text" class="emind-input" value="./output" placeholder="Choose directory">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Max Storage (GB)</label>
                            <input type="number" class="emind-input" value="5" min="1" max="100">
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="auto-cleanup" style="transform: scale(1.2);">
                            <label for="auto-cleanup" style="color: var(--text-secondary); font-weight: 500;">Auto-cleanup old files</label>
                        </div>
                    </div>
                </div>
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">Debug</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="debug-mode" style="transform: scale(1.2);">
                            <label for="debug-mode" style="color: var(--text-secondary); font-weight: 500;">Enable debug mode</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="verbose-logging" style="transform: scale(1.2);">
                            <label for="verbose-logging" style="color: var(--text-secondary); font-weight: 500;">Verbose logging</label>
                        </div>
                        <button class="emind-btn" style="align-self: flex-start; background: var(--warning-color);">
                            Export Logs
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """
        
        gr.HTML(advanced_settings_html)
        
        # Action buttons
        action_buttons_html = """
        <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
            <button class="emind-btn" style="background: var(--success-color);">
                Save All Settings
            </button>
            <button class="emind-btn" style="background: var(--bg-secondary); color: var(--text-primary); border: 2px solid var(--border-color);">
                Reset to Defaults
            </button>
            <button class="emind-btn" style="background: var(--error-color);">
                Clear All Data
            </button>
        </div>
        """
        
        gr.HTML(action_buttons_html)
    
    return settings_tab


def create_modern_settings_demo():
    """Create a demo of the modern settings page"""
    with gr.Blocks(
        title="EMIND - Modern Settings",
        css_file="emind/ui/web/components/styles/modern_theme.css",
        theme=gr.themes.Soft()
    ) as demo:
        create_modern_settings_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_modern_settings_demo()
    demo.launch(server_name="0.0.0.0", server_port=8025)
