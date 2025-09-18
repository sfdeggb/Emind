"""
EMIND 现代化首页 - 中文界面
"""

import gradio as gr
from ..components.modern_components import ModernUIComponents, ModernLayout


def create_modern_index_ui():
    """创建现代化首页"""
    
    # 头部
    header = ModernUIComponents.create_header(
        title="🎧 EMIND",
        subtitle="您的AI音乐创作伙伴 - 创作、发现、享受音乐"
    )
    
    # 主题切换
    theme_toggle = ModernUIComponents.create_theme_toggle()
    
    # 功能特性
    features = [
        {
            "title": "AI音乐生成",
            "description": "使用先进的AI模型，从文本描述、歌词或情感中生成原创音乐。",
            "icon": "🎵"
        },
        {
            "title": "情感分析",
            "description": "分析您的心情，生成与您当前情感状态相匹配的音乐。",
            "icon": "😊"
        },
        {
            "title": "语音合成",
            "description": "将文本转换为自然流畅的语音，为您的音乐添加人声。",
            "icon": "🎤"
        },
        {
            "title": "音乐处理",
            "description": "分离音轨、转换格式，使用专业工具增强您的音频。",
            "icon": "🎛️"
        },
        {
            "title": "智能推荐",
            "description": "根据您的偏好和听歌历史，获得个性化的音乐推荐。",
            "icon": "🎯"
        },
        {
            "title": "协作功能",
            "description": "分享您的创作，与他人协作，发现新的音乐可能性。",
            "icon": "🤝"
        }
    ]
    
    feature_grid = ModernUIComponents.create_feature_grid(features)
    
    # 统计数据
    stats = {
        "已生成歌曲": "1,234",
        "满意用户": "567",
        "音乐时长": "89小时",
        "活跃会话": "23"
    }
    
    stats_dashboard = ModernUIComponents.create_stats_dashboard(stats)
    
    # 快速开始部分
    quick_start_html = """
    <div class="emind-card" style="text-align: center; padding: 3rem;">
        <h2 style="margin: 0 0 1rem 0; color: var(--text-primary); font-size: 2rem;">准备创作音乐了吗？</h2>
        <p style="margin: 0 0 2rem 0; color: var(--text-secondary); font-size: 1.125rem; line-height: 1.6;">
            开始您的音乐之旅，与EMIND一起。无需经验，只需要您的创造力！
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <button class="emind-btn" onclick="switchToChat()">
                <span style="margin-right: 0.5rem;">💬</span>
                开始对话
            </button>
            <button class="emind-btn secondary" onclick="switchToSettings()">
                <span style="margin-right: 0.5rem;">⚙️</span>
                查看设置
            </button>
        </div>
    </div>
    """
    
    # 工作原理部分
    how_it_works_html = """
    <div class="emind-card">
        <h2 style="margin: 0 0 2rem 0; color: var(--text-primary); text-align: center; font-size: 1.875rem;">工作原理</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
            <div style="text-align: center;">
                <div style="background: linear-gradient(135deg, var(--primary-color), var(--primary-dark)); color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 1.75rem; font-weight: bold; box-shadow: var(--shadow-lg);">1</div>
                <h3 style="margin: 0 0 0.75rem 0; color: var(--text-primary); font-size: 1.25rem;">描述您的想法</h3>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">告诉我们您想要创作什么样的音乐，或者描述您的心情。</p>
            </div>
            <div style="text-align: center;">
                <div style="background: linear-gradient(135deg, var(--secondary-color), var(--accent-color)); color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 1.75rem; font-weight: bold; box-shadow: var(--shadow-lg);">2</div>
                <h3 style="margin: 0 0 0.75rem 0; color: var(--text-primary); font-size: 1.25rem;">AI处理</h3>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">我们的AI分析您的需求，为您生成完美的音乐。</p>
            </div>
            <div style="text-align: center;">
                <div style="background: linear-gradient(135deg, var(--accent-color), var(--success-color)); color: white; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem; font-size: 1.75rem; font-weight: bold; box-shadow: var(--shadow-lg);">3</div>
                <h3 style="margin: 0 0 0.75rem 0; color: var(--text-primary); font-size: 1.25rem;">享受与分享</h3>
                <p style="margin: 0; color: var(--text-secondary); line-height: 1.6;">聆听您的创作，进行调整，并与世界分享。</p>
            </div>
        </div>
    </div>
    """
    
    # 用户评价部分
    testimonials_html = """
    <div class="emind-card">
        <h2 style="margin: 0 0 2rem 0; color: var(--text-primary); text-align: center; font-size: 1.875rem;">用户评价</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div style="text-align: center; padding: 1.5rem;">
                <div style="background: var(--bg-tertiary); border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">👤</div>
                <p style="margin: 0 0 1rem 0; color: var(--text-secondary); font-style: italic; line-height: 1.6;">"EMIND让我能够轻松创作出专业的音乐作品，即使我没有任何音乐背景！"</p>
                <strong style="color: var(--text-primary);">- 张小明</strong>
            </div>
            <div style="text-align: center; padding: 1.5rem;">
                <div style="background: var(--bg-tertiary); border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">👤</div>
                <p style="margin: 0 0 1rem 0; color: var(--text-secondary); font-style: italic; line-height: 1.6;">"AI生成的音乐质量超出我的预期，现在我可以专注于创意而不是技术细节。"</p>
                <strong style="color: var(--text-primary);">- 李小红</strong>
            </div>
            <div style="text-align: center; padding: 1.5rem;">
                <div style="background: var(--bg-tertiary); border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-size: 1.5rem;">👤</div>
                <p style="margin: 0 0 1rem 0; color: var(--text-secondary); font-style: italic; line-height: 1.6;">"界面设计非常现代和直观，使用起来很愉快。强烈推荐！"</p>
                <strong style="color: var(--text-primary);">- 王小强</strong>
            </div>
        </div>
    </div>
    """
    
    # 页脚
    footer_html = """
    <div style="text-align: center; padding: 3rem 0; margin-top: 4rem; border-top: 1px solid var(--border-color);">
        <p style="margin: 0; color: var(--text-muted); font-size: 1rem;">
            由EMIND团队用 ❤️ 制作 | 
            <a href="#" style="color: var(--primary-color); text-decoration: none; font-weight: 500;">隐私政策</a> | 
            <a href="#" style="color: var(--primary-color); text-decoration: none; font-weight: 500;">服务条款</a>
        </p>
        <p style="margin: 1rem 0 0 0; color: var(--text-muted); font-size: 0.875rem;">
            © 2024 EMIND. 保留所有权利。
        </p>
    </div>
    """
    
    # 创建布局
    with gr.Tab("🏠 首页", elem_id="home_tab") as home_tab:
        header
        theme_toggle
        feature_grid
        stats_dashboard
        gr.HTML(quick_start_html)
        gr.HTML(how_it_works_html)
        gr.HTML(testimonials_html)
        gr.HTML(footer_html)
    
    # 添加JavaScript功能
    js_code = """
    <script>
        function switchToChat() {
            // 切换到聊天标签页
            const chatTab = document.querySelector('[data-testid="tab-chat_tab"]');
            if (chatTab) {
                chatTab.click();
            }
        }
        
        function switchToSettings() {
            // 切换到设置标签页
            const settingsTab = document.querySelector('[data-testid="tab-settings_tab"]');
            if (settingsTab) {
                settingsTab.click();
            }
        }
        
        function showNotification(message, type = 'info', duration = 3000) {
            const notification = document.createElement('div');
            notification.className = `emind-notification ${type}`;
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: var(--bg-card);
                border: 1px solid var(--border-light);
                border-left: 4px solid var(--primary-color);
                border-radius: var(--radius-xl);
                padding: 1rem 1.5rem;
                box-shadow: var(--shadow-xl);
                z-index: 10000;
                animation: slideInRight 0.4s ease-out;
                max-width: 350px;
                backdrop-filter: blur(10px);
            `;
            
            const colors = {
                info: 'var(--info-color)',
                success: 'var(--success-color)',
                warning: 'var(--warning-color)',
                error: 'var(--error-color)'
            };
            
            notification.style.borderLeftColor = colors[type] || colors.info;
            notification.innerHTML = `
                <div style="display: flex; align-items: center;">
                    <span style="margin-right: 0.5rem; font-size: 1.2rem;">${type === 'success' ? '✅' : type === 'warning' ? '⚠️' : type === 'error' ? '❌' : 'ℹ️'}</span>
                    <span style="color: var(--text-primary); font-weight: 500;">${message}</span>
                </div>
            `;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideOut 0.3s ease-in';
                setTimeout(() => {
                    if (notification.parentNode) {
                        notification.parentNode.removeChild(notification);
                    }
                }, 300);
            }, duration);
        }
        
        // 添加slideOut动画
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideOut {
                from {
                    opacity: 1;
                    transform: translateX(0);
                }
                to {
                    opacity: 0;
                    transform: translateX(100%);
                }
            }
        `;
        document.head.appendChild(style);
        
        // 页面加载完成后的初始化
        document.addEventListener('DOMContentLoaded', function() {
            // 添加滚动动画效果
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animation = 'slideInUp 0.6s ease-out';
                    }
                });
            }, observerOptions);
            
            // 观察所有卡片元素
            document.querySelectorAll('.emind-card').forEach(card => {
                observer.observe(card);
            });
        });
    </script>
    """
    
    gr.HTML(js_code)
    
    return home_tab


def create_modern_index_demo():
    """创建现代化首页演示"""
    with gr.Blocks(
        title="EMIND - 现代化首页"
        ,
        theme=gr.themes.Soft()
    ) as demo:
        create_modern_index_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_modern_index_demo()
    demo.launch(server_name="0.0.0.0", server_port=8023)
