"""
EMIND 现代化Web服务器 - 完整集成版本
"""

import gradio as gr
import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from .pages.modern_index import create_modern_index_ui
from .pages.modern_chat_integrated import IntegratedChatInterface
from .pages.modern_settings import create_modern_settings_ui
from .components.modern_components import ModernUIComponents


def create_modern_emind_app():
    """创建现代化EMIND应用程序"""
    
    # 初始化集成聊天界面
    chat_interface = IntegratedChatInterface()
    
    # 读取CSS文件内容
    css_path = Path(__file__).parent / "components" / "styles" / "modern_theme.css"
    css_content = ""
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    
    # 创建主应用
    with gr.Blocks(
        title="🎧 EMIND - 您的AI音乐创作伙伴",
        theme=gr.themes.Soft(),
        analytics_enabled=False
    ) as app:
        
        # 注入CSS样式
        if css_content:
            gr.HTML(f"<style>{css_content}</style>")
        
        # 主题切换（全局）
        theme_toggle = ModernUIComponents.create_theme_toggle()
        
        # 主导航
        with gr.Tabs(elem_id="main_tabs"):
            # 首页标签页
            home_tab = create_modern_index_ui()
            
            # 聊天标签页
            chat_tab = chat_interface.create_chat_ui()
            
            # 设置标签页
            settings_tab = create_modern_settings_ui()
        
        # 全局JavaScript
        global_js = """
        <script>
            // 全局主题管理
            function toggleTheme() {
                const body = document.body;
                const currentTheme = body.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                const themeIcon = document.getElementById('theme-icon');
                
                body.setAttribute('data-theme', newTheme);
                if (themeIcon) {
                    themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
                }
                
                // 保存主题偏好
                localStorage.setItem('emind-theme', newTheme);
                
                // 显示切换通知
                showNotification(`已切换到${newTheme === 'dark' ? '深色' : '浅色'}主题`, 'success');
            }
            
            // 页面加载时加载保存的主题
            document.addEventListener('DOMContentLoaded', function() {
                const savedTheme = localStorage.getItem('emind-theme') || 'light';
                document.body.setAttribute('data-theme', savedTheme);
                const themeIcon = document.getElementById('theme-icon');
                if (themeIcon) {
                    themeIcon.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
                }
            });
            
            // 平滑滚动锚点链接
            document.addEventListener('click', function(e) {
                if (e.target.tagName === 'A' && e.target.getAttribute('href') && e.target.getAttribute('href').startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(e.target.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
            
            // 自动保存表单数据
            function autoSaveForm(formId) {
                const form = document.getElementById(formId);
                if (form) {
                    const inputs = form.querySelectorAll('input, select, textarea');
                    inputs.forEach(input => {
                        input.addEventListener('change', function() {
                            const formData = new FormData(form);
                            const data = Object.fromEntries(formData);
                            localStorage.setItem(`emind-form-${formId}`, JSON.stringify(data));
                        });
                    });
                    
                    // 加载保存的数据
                    const savedData = localStorage.getItem(`emind-form-${formId}`);
                    if (savedData) {
                        const data = JSON.parse(savedData);
                        Object.keys(data).forEach(key => {
                            const input = form.querySelector(`[name="${key}"]`);
                            if (input) {
                                input.value = data[key];
                            }
                        });
                    }
                }
            }
            
            // 初始化所有表单的自动保存
            document.addEventListener('DOMContentLoaded', function() {
                const forms = document.querySelectorAll('form');
                forms.forEach(form => {
                    if (form.id) {
                        autoSaveForm(form.id);
                    }
                });
            });
            
            // 通知系统
            function showNotification(message, type = 'info', duration = 3000) {
                const notification = document.createElement('div');
                notification.className = `emind-notification notification-${type}`;
                notification.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: var(--bg-card);
                    border: 1px solid var(--border-light);
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
                
                const icons = {
                    info: 'ℹ️',
                    success: '✅',
                    warning: '⚠️',
                    error: '❌'
                };
                
                notification.style.borderLeftColor = colors[type] || colors.info;
                notification.innerHTML = `
                    <div style="display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem; font-size: 1.2rem;">${icons[type] || icons.info}</span>
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
            
            // 全局错误处理
            window.addEventListener('error', function(e) {
                console.error('全局错误:', e.error);
                showNotification('发生错误，请重试。', 'error');
            });
            
            // 服务工作者注册（用于PWA功能）
            if ('serviceWorker' in navigator) {
                window.addEventListener('load', function() {
                    navigator.serviceWorker.register('/sw.js')
                        .then(function(registration) {
                            console.log('ServiceWorker注册成功');
                        })
                        .catch(function(err) {
                            console.log('ServiceWorker注册失败');
                        });
                });
            }
            
            // 键盘快捷键
            document.addEventListener('keydown', function(e) {
                // Ctrl/Cmd + K 打开搜索
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    const input = document.getElementById('user_input');
                    if (input) {
                        input.focus();
                    }
                }
                
                // Esc 键清除焦点
                if (e.key === 'Escape') {
                    document.activeElement.blur();
                }
            });
            
            // 页面可见性变化处理
            document.addEventListener('visibilitychange', function() {
                if (document.hidden) {
                    // 页面隐藏时暂停动画
                    document.body.style.animationPlayState = 'paused';
                } else {
                    // 页面显示时恢复动画
                    document.body.style.animationPlayState = 'running';
                }
            });
            
            // 网络状态检测
            window.addEventListener('online', function() {
                showNotification('网络连接已恢复', 'success');
            });
            
            window.addEventListener('offline', function() {
                showNotification('网络连接已断开', 'warning');
            });
            
            // 性能监控
            if ('performance' in window) {
                window.addEventListener('load', function() {
                    setTimeout(function() {
                        const perfData = performance.getEntriesByType('navigation')[0];
                        if (perfData) {
                            const loadTime = perfData.loadEventEnd - perfData.loadEventStart;
                            console.log(`页面加载时间: ${loadTime}ms`);
                        }
                    }, 0);
                });
            }
        </script>
        """
        
        gr.HTML(global_js)
    
    return app


def main(config_path: str = "config/default.yaml", port: int = 8022, debug: bool = False):
    """运行EMIND服务器的主函数"""
    print("🎧 启动EMIND现代化Web界面...")
    print(f"📁 配置文件: {config_path}")
    print(f"🌐 端口: {port}")
    print(f"🐛 调试模式: {debug}")
    
    # 检查配置文件是否存在
    if not os.path.exists(config_path):
        print(f"⚠️  配置文件不存在: {config_path}")
        print("使用默认配置...")
    
    # 创建应用
    app = create_modern_emind_app()
    
    # 启动应用
    app.queue().launch(
        server_name="0.0.0.0",
        server_port=port,
        debug=debug,
        show_error=debug,
        share=False,
        inbrowser=True
    )


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="EMIND现代化Web界面")
    parser.add_argument("--config", default="config/default.yaml", help="配置文件路径")
    parser.add_argument("--port", type=int, default=8022, help="服务器端口")
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    
    args = parser.parse_args()
    
    main(args.config, args.port, args.debug)
