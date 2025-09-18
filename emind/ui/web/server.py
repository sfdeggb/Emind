"""
Modern EMIND Web Server
"""

import gradio as gr
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from .pages.modern_index import create_modern_index_ui
from .pages.modern_chat import ModernChatInterface
from .pages.modern_settings import create_modern_settings_ui
from .components.modern_components import ModernUIComponents


def create_modern_emind_app():
    """Create the modern EMIND application"""
    
    # Initialize chat interface
    chat_interface = ModernChatInterface()
    
    # Create the main app
    with gr.Blocks(
        title="🎧 EMIND - Your AI Music Companion",
        css_file="emind/ui/web/components/styles/modern_theme.css",
        theme=gr.themes.Soft(),
        analytics_enabled=False
    ) as app:
        
        # Theme toggle (global)
        theme_toggle = ModernUIComponents.create_theme_toggle()
        
        # Main navigation
        with gr.Tabs(elem_id="main_tabs"):
            # Home tab
            home_tab = create_modern_index_ui()
            
            # Chat tab
            chat_tab = chat_interface.create_chat_ui()
            
            # Settings tab
            settings_tab = create_modern_settings_ui()
        
        # Global JavaScript
        global_js = """
        <script>
            // Global theme management
            function toggleTheme() {
                const body = document.body;
                const currentTheme = body.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                const themeIcon = document.getElementById('theme-icon');
                
                body.setAttribute('data-theme', newTheme);
                if (themeIcon) {
                    themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
                }
                
                // Save theme preference
                localStorage.setItem('emind-theme', newTheme);
            }
            
            // Load saved theme on page load
            document.addEventListener('DOMContentLoaded', function() {
                const savedTheme = localStorage.getItem('emind-theme') || 'light';
                document.body.setAttribute('data-theme', savedTheme);
                const themeIcon = document.getElementById('theme-icon');
                if (themeIcon) {
                    themeIcon.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
                }
            });
            
            // Smooth scrolling for anchor links
            document.addEventListener('click', function(e) {
                if (e.target.tagName === 'A' && e.target.getAttribute('href').startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(e.target.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
            
            // Auto-save form data
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
                    
                    // Load saved data
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
            
            // Initialize auto-save for all forms
            document.addEventListener('DOMContentLoaded', function() {
                const forms = document.querySelectorAll('form');
                forms.forEach(form => {
                    if (form.id) {
                        autoSaveForm(form.id);
                    }
                });
            });
            
            // Notification system
            function showNotification(message, type = 'info', duration = 3000) {
                const notification = document.createElement('div');
                notification.className = `notification notification-${type}`;
                notification.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: var(--bg-secondary);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-lg);
                    padding: 1rem;
                    box-shadow: var(--shadow-lg);
                    z-index: 10000;
                    animation: slideIn 0.3s ease-out;
                    max-width: 300px;
                `;
                
                const colors = {
                    info: 'var(--primary-color)',
                    success: 'var(--success-color)',
                    warning: 'var(--warning-color)',
                    error: 'var(--error-color)'
                };
                
                notification.style.borderLeftColor = colors[type] || colors.info;
                notification.textContent = message;
                
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
            
            // Add slideOut animation
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
            
            // Global error handler
            window.addEventListener('error', function(e) {
                console.error('Global error:', e.error);
                showNotification('An error occurred. Please try again.', 'error');
            });
            
            // Service worker registration (for PWA features)
            if ('serviceWorker' in navigator) {
                window.addEventListener('load', function() {
                    navigator.serviceWorker.register('/sw.js')
                        .then(function(registration) {
                            console.log('ServiceWorker registration successful');
                        })
                        .catch(function(err) {
                            console.log('ServiceWorker registration failed');
                        });
                });
            }
        </script>
        """
        
        gr.HTML(global_js)
    
    return app


def main(config_path: str = "config/default.yaml", port: int = 8022, debug: bool = False):
    """Main function to run the EMIND server"""
    print("🎧 Starting EMIND Modern Web Interface...")
    print(f"📁 Config: {config_path}")
    print(f"🌐 Port: {port}")
    print(f"🐛 Debug: {debug}")
    
    # Create the app
    app = create_modern_emind_app()
    
    # Launch the app
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
    
    parser = argparse.ArgumentParser(description="EMIND Modern Web Interface")
    parser.add_argument("--config", default="config/default.yaml", help="Configuration file path")
    parser.add_argument("--port", type=int, default=8022, help="Server port")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    main(args.config, args.port, args.debug)
