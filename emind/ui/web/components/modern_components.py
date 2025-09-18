"""
Modern UI Components for Emind
"""

import gradio as gr
from typing import Optional, List, Dict, Any
import json


class ModernUIComponents:
    """Modern UI components for Emind interface"""
    
    @staticmethod
    def create_header(title: str = "🎧 EMIND", subtitle: str = "Your AI Music Companion") -> gr.HTML:
        """Create a modern header component"""
        header_html = f"""
        <div class="emind-header">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """
        return gr.HTML(header_html)
    
    @staticmethod
    def create_feature_card(title: str, description: str, icon: str = "🎵") -> gr.HTML:
        """Create a feature card component"""
        card_html = f"""
        <div class="emind-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
                <h3 style="margin: 0; color: var(--text-primary);">{title}</h3>
            </div>
            <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">{description}</p>
        </div>
        """
        return gr.HTML(card_html)
    
    @staticmethod
    def create_audio_player(audio_path: str, title: str = "Generated Audio") -> gr.HTML:
        """Create a modern audio player component"""
        player_html = f"""
        <div class="emind-audio-player">
            <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">{title}</h4>
            <audio controls style="width: 100%; border-radius: var(--radius-lg);">
                <source src="{audio_path}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <div class="emind-audio-controls">
                <button class="emind-play-btn" onclick="togglePlay()">
                    <span id="play-icon">▶</span>
                </button>
                <div class="emind-progress">
                    <div class="emind-progress-bar" id="progress-bar" style="width: 0%;"></div>
                </div>
                <span id="time-display" style="color: var(--text-secondary); font-size: 0.875rem;">0:00 / 0:00</span>
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
    def create_loading_spinner(text: str = "Processing...") -> gr.HTML:
        """Create a loading spinner component"""
        spinner_html = f"""
        <div class="emind-loading" style="justify-content: center; padding: 2rem;">
            <div class="emind-spinner"></div>
            <span style="margin-left: 0.5rem; color: var(--text-secondary);">{text}</span>
        </div>
        """
        return gr.HTML(spinner_html)
    
    @staticmethod
    def create_progress_bar(progress: float = 0.0, text: str = "") -> gr.HTML:
        """Create a progress bar component"""
        progress_html = f"""
        <div style="margin: 1rem 0;">
            <div class="emind-progress">
                <div class="emind-progress-bar" style="width: {progress * 100}%;"></div>
            </div>
            {f'<p style="text-align: center; margin: 0.5rem 0; color: var(--text-secondary);">{text}</p>' if text else ''}
        </div>
        """
        return gr.HTML(progress_html)
    
    @staticmethod
    def create_message_bubble(message: str, sender: str = "assistant", timestamp: str = "") -> gr.HTML:
        """Create a message bubble component"""
        sender_class = sender.lower()
        time_html = f'<small style="opacity: 0.7; font-size: 0.75rem;">{timestamp}</small>' if timestamp else ''
        
        bubble_html = f"""
        <div class="emind-message {sender_class}">
            <div style="margin-bottom: 0.5rem;">{message}</div>
            {time_html}
        </div>
        """
        return gr.HTML(bubble_html)
    
    @staticmethod
    def create_feature_grid(features: List[Dict[str, str]]) -> gr.HTML:
        """Create a grid of feature cards"""
        cards_html = ""
        for feature in features:
            title = feature.get('title', '')
            description = feature.get('description', '')
            icon = feature.get('icon', '🎵')
            cards_html += f"""
            <div class="emind-card" style="margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
                    <h3 style="margin: 0; color: var(--text-primary);">{title}</h3>
                </div>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">{description}</p>
            </div>
            """
        
        grid_html = f"""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
            {cards_html}
        </div>
        """
        return gr.HTML(grid_html)
    
    @staticmethod
    def create_theme_toggle() -> gr.HTML:
        """Create a theme toggle button"""
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
                
                // Save theme preference
                localStorage.setItem('emind-theme', newTheme);
            }
            
            // Load saved theme
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
        """Create a statistics dashboard"""
        stats_html = ""
        for key, value in stats.items():
            stats_html += f"""
            <div class="emind-card" style="text-align: center; padding: 1.5rem;">
                <h2 style="margin: 0; color: var(--primary-color); font-size: 2rem;">{value}</h2>
                <p style="margin: 0.5rem 0 0 0; color: var(--text-secondary); text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em;">{key}</p>
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
        """Create a notification component"""
        type_colors = {
            "info": "var(--primary-color)",
            "success": "var(--success-color)",
            "warning": "var(--warning-color)",
            "error": "var(--error-color)"
        }
        
        color = type_colors.get(type, "var(--primary-color)")
        
        notification_html = f"""
        <div style="
            background: var(--bg-secondary);
            border-left: 4px solid {color};
            border-radius: var(--radius-lg);
            padding: 1rem;
            margin: 1rem 0;
            box-shadow: var(--shadow-sm);
            animation: slideIn 0.3s ease-out;
        ">
            <p style="margin: 0; color: var(--text-primary);">{message}</p>
        </div>
        """
        return gr.HTML(notification_html)


class ModernLayout:
    """Modern layout utilities"""
    
    @staticmethod
    def create_sidebar_layout(sidebar_content: List[Any], main_content: List[Any]) -> gr.Blocks:
        """Create a sidebar layout"""
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
        """Create a centered layout"""
        with gr.Blocks(css_file="emind/ui/web/components/styles/modern_theme.css") as layout:
            gr.HTML(f'<div style="max-width: {max_width}; margin: 0 auto; padding: 2rem;">')
            for item in content:
                item
            gr.HTML('</div>')
        
        return layout
    
    @staticmethod
    def create_tabbed_layout(tabs: Dict[str, List[Any]]) -> gr.Blocks:
        """Create a tabbed layout"""
        with gr.Blocks(css_file="emind/ui/web/components/styles/modern_theme.css") as layout:
            with gr.Tabs():
                for tab_name, tab_content in tabs.items():
                    with gr.Tab(tab_name):
                        for content in tab_content:
                            content
        
        return layout
