"""
修复版本的现代首页 - 解决依赖问题
"""

import gradio as gr
import os

def create_modern_header(title="🎧 EMIND", subtitle="Your AI Music Companion"):
    """创建现代化头部"""
    header_html = f"""
    <div style="
        background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    ">
        <h1 style="margin: 0; font-size: 2.5rem; font-weight: 800;">{title}</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">{subtitle}</p>
    </div>
    """
    return gr.HTML(header_html)

def create_feature_card(title, description, icon="🎵"):
    """创建功能卡片"""
    card_html = f"""
    <div style="
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 1rem;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    " onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 4px 12px rgba(0, 0, 0, 0.15)'" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0, 0, 0, 0.1)'">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="font-size: 2rem; margin-right: 1rem;">{icon}</span>
            <h3 style="margin: 0; color: #1e293b;">{title}</h3>
        </div>
        <p style="margin: 0; color: #64748b; line-height: 1.6;">{description}</p>
    </div>
    """
    return gr.HTML(card_html)

def create_modern_index_ui():
    """创建现代化首页"""
    
    # 现代化CSS
    css = """
    .gradio-container {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        background: #ffffff !important;
    }
    
    .gradio-container .tab-nav {
        background: #f8fafc !important;
        border-radius: 1rem !important;
        padding: 0.5rem !important;
        margin-bottom: 2rem !important;
    }
    
    .gradio-container .tab-nav button {
        background: transparent !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem 1.5rem !important;
        margin: 0 0.25rem !important;
        font-weight: 500 !important;
        color: #64748b !important;
        transition: all 0.3s ease !important;
    }
    
    .gradio-container .tab-nav button.selected {
        background: #6366f1 !important;
        color: white !important;
        box-shadow: 0 2px 4px rgba(99, 102, 241, 0.3) !important;
    }
    
    .gradio-container .tab-nav button:hover:not(.selected) {
        background: #f1f5f9 !important;
        color: #1e293b !important;
    }
    
    .gradio-container .btn {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 4px rgba(99, 102, 241, 0.2) !important;
    }
    
    .gradio-container .btn:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3) !important;
    }
    
    .gradio-container .textbox {
        background: #ffffff !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 0.5rem !important;
        color: #1e293b !important;
        transition: all 0.3s ease !important;
    }
    
    .gradio-container .textbox:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    }
    """
    
    with gr.Blocks(css=css, title="🎧 EMIND - Modern Home") as demo:
        
        with gr.Tab("🏠 Home", elem_id="home_tab"):
            
            # 头部
            header = create_modern_header()
            
            # 功能展示
            features = [
                ("AI Music Generation", "Generate original music from text descriptions, lyrics, or emotions using advanced AI models.", "🎵"),
                ("Emotion Analysis", "Analyze your mood and generate music that matches your current emotional state.", "😊"),
                ("Voice Synthesis", "Convert text to speech with natural-sounding voices for your generated music.", "🎤"),
                ("Music Processing", "Separate tracks, convert formats, and enhance your audio with professional tools.", "🎛️"),
                ("Smart Recommendations", "Get personalized music recommendations based on your preferences and listening history.", "🎯"),
                ("Collaborative Features", "Share your creations, collaborate with others, and discover new musical possibilities.", "🤝")
            ]
            
            for title, description, icon in features:
                create_feature_card(title, description, icon)
            
            # 统计数据
            stats_html = """
            <div style="
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); 
                gap: 1.5rem; 
                margin: 2rem 0;
            ">
                <div style="
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 1rem;
                    padding: 2rem;
                    text-align: center;
                    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                ">
                    <h2 style="margin: 0; color: #6366f1; font-size: 2rem;">1,234</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #64748b; text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em;">Songs Generated</p>
                </div>
                <div style="
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 1rem;
                    padding: 2rem;
                    text-align: center;
                    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                ">
                    <h2 style="margin: 0; color: #ec4899; font-size: 2rem;">567</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #64748b; text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em;">Happy Users</p>
                </div>
                <div style="
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 1rem;
                    padding: 2rem;
                    text-align: center;
                    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                ">
                    <h2 style="margin: 0; color: #06b6d4; font-size: 2rem;">89</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #64748b; text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em;">Hours of Music</p>
                </div>
                <div style="
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 1rem;
                    padding: 2rem;
                    text-align: center;
                    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                ">
                    <h2 style="margin: 0; color: #10b981; font-size: 2rem;">23</h2>
                    <p style="margin: 0.5rem 0 0 0; color: #64748b; text-transform: uppercase; font-size: 0.875rem; letter-spacing: 0.05em;">Active Sessions</p>
                </div>
            </div>
            """
            gr.HTML(stats_html)
            
            # 快速开始
            quick_start_html = """
            <div style="
                background: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: 1rem;
                padding: 3rem;
                text-align: center;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
                margin: 2rem 0;
            ">
                <h2 style="margin: 0 0 1rem 0; color: #1e293b;">Ready to Create Music?</h2>
                <p style="margin: 0 0 2rem 0; color: #64748b; font-size: 1.125rem;">
                    Start your musical journey with EMIND. No experience required - just your creativity!
                </p>
                <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                    <button class="emind-btn" onclick="window.location.href='#chat'" style="
                        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
                        color: white;
                        border: none;
                        border-radius: 0.5rem;
                        padding: 0.75rem 1.5rem;
                        font-weight: 600;
                        cursor: pointer;
                        transition: all 0.3s ease;
                    ">
                        Start Chatting
                    </button>
                    <button class="emind-btn" onclick="window.location.href='#settings'" style="
                        background: #f8fafc;
                        color: #1e293b;
                        border: 2px solid #e2e8f0;
                        border-radius: 0.5rem;
                        padding: 0.75rem 1.5rem;
                        font-weight: 600;
                        cursor: pointer;
                        transition: all 0.3s ease;
                    ">
                        View Settings
                    </button>
                </div>
            </div>
            """
            gr.HTML(quick_start_html)
            
            # 使用指南
            how_it_works_html = """
            <div style="
                background: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: 1rem;
                padding: 2rem;
                margin: 2rem 0;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            ">
                <h2 style="margin: 0 0 2rem 0; color: #1e293b; text-align: center;">How It Works</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
                    <div style="text-align: center;">
                        <div style="
                            background: #6366f1;
                            color: white;
                            width: 60px;
                            height: 60px;
                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0 auto 1rem;
                            font-size: 1.5rem;
                            font-weight: bold;
                        ">1</div>
                        <h3 style="margin: 0 0 0.5rem 0; color: #1e293b;">Describe Your Vision</h3>
                        <p style="margin: 0; color: #64748b;">Tell us what kind of music you want to create or describe your mood.</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="
                            background: #ec4899;
                            color: white;
                            width: 60px;
                            height: 60px;
                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0 auto 1rem;
                            font-size: 1.5rem;
                            font-weight: bold;
                        ">2</div>
                        <h3 style="margin: 0 0 0.5rem 0; color: #1e293b;">AI Processing</h3>
                        <p style="margin: 0; color: #64748b;">Our AI analyzes your request and generates the perfect music for you.</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="
                            background: #06b6d4;
                            color: white;
                            width: 60px;
                            height: 60px;
                            border-radius: 50%;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin: 0 auto 1rem;
                            font-size: 1.5rem;
                            font-weight: bold;
                        ">3</div>
                        <h3 style="margin: 0 0 0.5rem 0; color: #1e293b;">Enjoy & Share</h3>
                        <p style="margin: 0; color: #64748b;">Listen to your creation, make adjustments, and share with the world.</p>
                    </div>
                </div>
            </div>
            """
            gr.HTML(how_it_works_html)
            
            # 页脚
            footer_html = """
            <div style="
                text-align: center; 
                padding: 3rem 0; 
                margin-top: 4rem; 
                border-top: 1px solid #e2e8f0;
            ">
                <p style="margin: 0; color: #94a3b8;">
                    Made with ❤️ by the EMIND Team | 
                    <a href="#" style="color: #6366f1; text-decoration: none;">Privacy Policy</a> | 
                    <a href="#" style="color: #6366f1; text-decoration: none;">Terms of Service</a>
                </p>
                <p style="margin: 1rem 0 0 0; color: #94a3b8; font-size: 0.875rem;">
                    © 2024 EMIND. All rights reserved.
                </p>
            </div>
            """
            gr.HTML(footer_html)
    
    return demo

if __name__ == "__main__":
    print("🎧 Starting EMIND Modern Index...")
    demo = create_modern_index_ui()
    demo.launch(server_name="0.0.0.0", server_port=8027, inbrowser=True)
