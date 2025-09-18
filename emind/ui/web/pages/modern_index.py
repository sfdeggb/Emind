"""
Modern Index Page for Emind
"""

import gradio as gr
from ..components.modern_components import ModernUIComponents, ModernLayout


def create_modern_index_ui():
    """Create a modern index page"""
    
    # Header
    header = ModernUIComponents.create_header(
        title="🎧 EMIND",
        subtitle="Your AI Music Companion - Create, Discover, and Enjoy Music"
    )
    
    # Theme toggle
    theme_toggle = ModernUIComponents.create_theme_toggle()
    
    # Features
    features = [
        {
            "title": "AI Music Generation",
            "description": "Generate original music from text descriptions, lyrics, or emotions using advanced AI models.",
            "icon": "🎵"
        },
        {
            "title": "Emotion Analysis",
            "description": "Analyze your mood and generate music that matches your current emotional state.",
            "icon": "😊"
        },
        {
            "title": "Voice Synthesis",
            "description": "Convert text to speech with natural-sounding voices for your generated music.",
            "icon": "🎤"
        },
        {
            "title": "Music Processing",
            "description": "Separate tracks, convert formats, and enhance your audio with professional tools.",
            "icon": "🎛️"
        },
        {
            "title": "Smart Recommendations",
            "description": "Get personalized music recommendations based on your preferences and listening history.",
            "icon": "🎯"
        },
        {
            "title": "Collaborative Features",
            "description": "Share your creations, collaborate with others, and discover new musical possibilities.",
            "icon": "🤝"
        }
    ]
    
    feature_grid = ModernUIComponents.create_feature_grid(features)
    
    # Statistics
    stats = {
        "Songs Generated": "1,234",
        "Happy Users": "567",
        "Hours of Music": "89",
        "Active Sessions": "23"
    }
    
    stats_dashboard = ModernUIComponents.create_stats_dashboard(stats)
    
    # Quick start section
    quick_start_html = """
    <div class="emind-card" style="text-align: center; padding: 3rem;">
        <h2 style="margin: 0 0 1rem 0; color: var(--text-primary);">Ready to Create Music?</h2>
        <p style="margin: 0 0 2rem 0; color: var(--text-secondary); font-size: 1.125rem;">
            Start your musical journey with EMIND. No experience required - just your creativity!
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <button class="emind-btn" onclick="window.location.href='#chat'">
                Start Chatting
            </button>
            <button class="emind-btn" onclick="window.location.href='#settings'" style="background: var(--bg-secondary); color: var(--text-primary); border: 2px solid var(--border-color);">
                View Settings
            </button>
        </div>
    </div>
    """
    
    # How it works section
    how_it_works_html = """
    <div class="emind-card">
        <h2 style="margin: 0 0 2rem 0; color: var(--text-primary); text-align: center;">How It Works</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <div style="text-align: center;">
                <div style="background: var(--primary-color); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">1</div>
                <h3 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">Describe Your Vision</h3>
                <p style="margin: 0; color: var(--text-secondary);">Tell us what kind of music you want to create or describe your mood.</p>
            </div>
            <div style="text-align: center;">
                <div style="background: var(--secondary-color); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">2</div>
                <h3 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">AI Processing</h3>
                <p style="margin: 0; color: var(--text-secondary);">Our AI analyzes your request and generates the perfect music for you.</p>
            </div>
            <div style="text-align: center;">
                <div style="background: var(--accent-color); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem; font-weight: bold;">3</div>
                <h3 style="margin: 0 0 0.5rem 0; color: var(--text-primary);">Enjoy & Share</h3>
                <p style="margin: 0; color: var(--text-secondary);">Listen to your creation, make adjustments, and share with the world.</p>
            </div>
        </div>
    </div>
    """
    
    # Footer
    footer_html = """
    <div style="text-align: center; padding: 3rem 0; margin-top: 4rem; border-top: 1px solid var(--border-color);">
        <p style="margin: 0; color: var(--text-muted);">
            Made with ❤️ by the EMIND Team | 
            <a href="#" style="color: var(--primary-color); text-decoration: none;">Privacy Policy</a> | 
            <a href="#" style="color: var(--primary-color); text-decoration: none;">Terms of Service</a>
        </p>
        <p style="margin: 1rem 0 0 0; color: var(--text-muted); font-size: 0.875rem;">
            © 2024 EMIND. All rights reserved.
        </p>
    </div>
    """
    
    # Create the layout
    with gr.Tab("🏠 Home", elem_id="home_tab") as home_tab:
        header
        theme_toggle
        feature_grid
        stats_dashboard
        gr.HTML(quick_start_html)
        gr.HTML(how_it_works_html)
        gr.HTML(footer_html)
    
    return home_tab


def create_modern_index_demo():
    """Create a demo of the modern index page"""
    with gr.Blocks(
        title="EMIND - Modern Home",
        css_file="emind/ui/web/components/styles/modern_theme.css",
        theme=gr.themes.Soft()
    ) as demo:
        create_modern_index_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_modern_index_demo()
    demo.launch(server_name="0.0.0.0", server_port=8023)
