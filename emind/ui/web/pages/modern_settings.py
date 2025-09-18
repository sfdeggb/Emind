"""
EMIND 现代化设置页面 - 中文界面
"""

import gradio as gr
from ..components.modern_components import ModernUIComponents


def create_modern_settings_ui():
    """创建现代化设置页面"""
    
    # 头部
    header = ModernUIComponents.create_header(
        title="⚙️ 设置",
        subtitle="自定义您的EMIND体验"
    )
    
    with gr.Tab("⚙️ 设置", elem_id="settings_tab") as settings_tab:
        header
        
        with gr.Row():
            with gr.Column(scale=2):
                # API配置
                api_config_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🔑</span>
                        API配置
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">OpenAI API密钥</label>
                            <input type="password" class="emind-input" placeholder="sk-..." style="font-family: monospace;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">HuggingFace令牌</label>
                            <input type="password" class="emind-input" placeholder="hf_..." style="font-family: monospace;">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Spotify客户端ID</label>
                            <input type="text" class="emind-input" placeholder="您的Spotify客户端ID">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">Google API密钥</label>
                            <input type="password" class="emind-input" placeholder="AIza...">
                        </div>
                        <button class="emind-btn" style="align-self: flex-start;">
                            <span style="margin-right: 0.5rem;">💾</span>
                            保存API密钥
                        </button>
                    </div>
                </div>
                """
                
                gr.HTML(api_config_html)
                
                # 模型设置
                model_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🤖</span>
                        模型设置
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">默认模型</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>GPT-3.5 Turbo</option>
                                <option>GPT-4</option>
                                <option>Claude-3</option>
                                <option>本地模型</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">音乐生成模型</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>MUZIC (推荐)</option>
                                <option>MusicLM</option>
                                <option>Jukebox</option>
                                <option>自定义模型</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">语音合成模型</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>DiffSinger</option>
                                <option>Tacotron2</option>
                                <option>FastSpeech2</option>
                                <option>自定义TTS</option>
                            </select>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="use-gpu" style="transform: scale(1.2);">
                            <label for="use-gpu" style="color: var(--text-secondary); font-weight: 500;">使用GPU加速</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(model_settings_html)
            
            with gr.Column(scale=1):
                # 音频设置
                audio_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🎵</span>
                        音频设置
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">采样率</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>44.1 kHz</option>
                                <option>48 kHz</option>
                                <option>96 kHz</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">位深度</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>16位</option>
                                <option>24位</option>
                                <option>32位</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">输出格式</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>MP3</option>
                                <option>WAV</option>
                                <option>FLAC</option>
                                <option>OGG</option>
                            </select>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="auto-download" style="transform: scale(1.2);">
                            <label for="auto-download" style="color: var(--text-secondary); font-weight: 500;">自动下载生成的文件</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(audio_settings_html)
                
                # 界面设置
                interface_settings_html = """
                <div class="emind-card">
                    <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                        <span style="margin-right: 0.5rem;">🎨</span>
                        界面设置
                    </h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">主题</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>浅色</option>
                                <option>深色</option>
                                <option>自动</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">语言</label>
                            <select class="emind-input" style="padding: 0.75rem;">
                                <option>中文</option>
                                <option>English</option>
                                <option>日本語</option>
                                <option>Español</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">字体大小</label>
                            <input type="range" min="12" max="20" value="16" class="emind-input" style="padding: 0;">
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="animations" style="transform: scale(1.2);" checked>
                            <label for="animations" style="color: var(--text-secondary); font-weight: 500;">启用动画效果</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="notifications" style="transform: scale(1.2);" checked>
                            <label for="notifications" style="color: var(--text-secondary); font-weight: 500;">显示通知</label>
                        </div>
                    </div>
                </div>
                """
                
                gr.HTML(interface_settings_html)
        
        # 高级设置
        advanced_settings_html = """
        <div class="emind-card">
            <h3 style="margin: 0 0 1.5rem 0; color: var(--text-primary); display: flex; align-items: center;">
                <span style="margin-right: 0.5rem;">🔧</span>
                高级设置
            </h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">性能</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">最大并发请求数</label>
                            <input type="number" class="emind-input" value="3" min="1" max="10">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">请求超时时间（秒）</label>
                            <input type="number" class="emind-input" value="30" min="5" max="300">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">缓存大小（MB）</label>
                            <input type="number" class="emind-input" value="100" min="10" max="1000">
                        </div>
                    </div>
                </div>
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">存储</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">输出目录</label>
                            <input type="text" class="emind-input" value="./output" placeholder="选择目录">
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem; color: var(--text-secondary); font-weight: 500;">最大存储空间（GB）</label>
                            <input type="number" class="emind-input" value="5" min="1" max="100">
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="auto-cleanup" style="transform: scale(1.2);">
                            <label for="auto-cleanup" style="color: var(--text-secondary); font-weight: 500;">自动清理旧文件</label>
                        </div>
                    </div>
                </div>
                <div>
                    <h4 style="margin: 0 0 1rem 0; color: var(--text-primary);">调试</h4>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="debug-mode" style="transform: scale(1.2);">
                            <label for="debug-mode" style="color: var(--text-secondary); font-weight: 500;">启用调试模式</label>
                        </div>
                        <div style="display: flex; align-items: center; gap: 1rem;">
                            <input type="checkbox" id="verbose-logging" style="transform: scale(1.2);">
                            <label for="verbose-logging" style="color: var(--text-secondary); font-weight: 500;">详细日志记录</label>
                        </div>
                        <button class="emind-btn" style="align-self: flex-start; background: var(--warning-color);">
                            <span style="margin-right: 0.5rem;">📤</span>
                            导出日志
                        </button>
                    </div>
                </div>
            </div>
        </div>
        """
        
        gr.HTML(advanced_settings_html)
        
        # 操作按钮
        action_buttons_html = """
        <div style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem; flex-wrap: wrap;">
            <button class="emind-btn" style="background: var(--success-color);">
                <span style="margin-right: 0.5rem;">💾</span>
                保存所有设置
            </button>
            <button class="emind-btn secondary">
                <span style="margin-right: 0.5rem;">🔄</span>
                重置为默认值
            </button>
            <button class="emind-btn" style="background: var(--error-color);">
                <span style="margin-right: 0.5rem;">🗑️</span>
                清除所有数据
            </button>
        </div>
        """
        
        gr.HTML(action_buttons_html)
    
    # 添加JavaScript功能
    js_code = """
    <script>
        // 设置保存功能
        function saveSettings() {
            const settings = {
                apiKeys: {
                    openai: document.querySelector('input[placeholder="sk-..."]').value,
                    huggingface: document.querySelector('input[placeholder="hf_..."]').value,
                    spotify: document.querySelector('input[placeholder="您的Spotify客户端ID"]').value,
                    google: document.querySelector('input[placeholder="AIza..."]').value
                },
                models: {
                    default: document.querySelector('select').value,
                    music: document.querySelectorAll('select')[1].value,
                    tts: document.querySelectorAll('select')[2].value,
                    gpu: document.getElementById('use-gpu').checked
                },
                audio: {
                    sampleRate: document.querySelectorAll('select')[3].value,
                    bitDepth: document.querySelectorAll('select')[4].value,
                    format: document.querySelectorAll('select')[5].value,
                    autoDownload: document.getElementById('auto-download').checked
                },
                interface: {
                    theme: document.querySelectorAll('select')[6].value,
                    language: document.querySelectorAll('select')[7].value,
                    fontSize: document.querySelector('input[type="range"]').value,
                    animations: document.getElementById('animations').checked,
                    notifications: document.getElementById('notifications').checked
                },
                advanced: {
                    maxRequests: document.querySelector('input[type="number"]').value,
                    timeout: document.querySelectorAll('input[type="number"]')[1].value,
                    cacheSize: document.querySelectorAll('input[type="number"]')[2].value,
                    outputDir: document.querySelectorAll('input[type="text"]')[1].value,
                    maxStorage: document.querySelectorAll('input[type="number"]')[3].value,
                    autoCleanup: document.getElementById('auto-cleanup').checked,
                    debugMode: document.getElementById('debug-mode').checked,
                    verboseLogging: document.getElementById('verbose-logging').checked
                }
            };
            
            localStorage.setItem('emind-settings', JSON.stringify(settings));
            showNotification('设置已保存！', 'success');
        }
        
        // 加载设置
        function loadSettings() {
            const savedSettings = localStorage.getItem('emind-settings');
            if (savedSettings) {
                const settings = JSON.parse(savedSettings);
                
                // 加载API密钥
                if (settings.apiKeys) {
                    document.querySelector('input[placeholder="sk-..."]').value = settings.apiKeys.openai || '';
                    document.querySelector('input[placeholder="hf_..."]').value = settings.apiKeys.huggingface || '';
                    document.querySelector('input[placeholder="您的Spotify客户端ID"]').value = settings.apiKeys.spotify || '';
                    document.querySelector('input[placeholder="AIza..."]').value = settings.apiKeys.google || '';
                }
                
                // 加载其他设置...
                showNotification('设置已加载！', 'info');
            }
        }
        
        // 重置设置
        function resetSettings() {
            if (confirm('确定要重置所有设置为默认值吗？')) {
                localStorage.removeItem('emind-settings');
                location.reload();
            }
        }
        
        // 清除数据
        function clearAllData() {
            if (confirm('确定要清除所有数据吗？此操作不可撤销！')) {
                localStorage.clear();
                showNotification('所有数据已清除！', 'warning');
            }
        }
        
        // 通知功能
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
        
        // 页面加载时初始化
        document.addEventListener('DOMContentLoaded', function() {
            loadSettings();
            
            // 绑定按钮事件
            const saveBtn = document.querySelector('button[style*="background: var(--success-color)"]');
            const resetBtn = document.querySelector('button[style*="background: var(--bg-secondary)"]');
            const clearBtn = document.querySelector('button[style*="background: var(--error-color)"]');
            
            if (saveBtn) saveBtn.onclick = saveSettings;
            if (resetBtn) resetBtn.onclick = resetSettings;
            if (clearBtn) clearBtn.onclick = clearAllData;
        });
    </script>
    """
    
    gr.HTML(js_code)
    
    return settings_tab


def create_modern_settings_demo():
    """创建现代化设置页面演示"""
    with gr.Blocks(
        title="EMIND - 现代化设置"
        ,
        theme=gr.themes.Soft()
    ) as demo:
        create_modern_settings_ui()
    
    return demo


if __name__ == "__main__":
    demo = create_modern_settings_demo()
    demo.launch(server_name="0.0.0.0", server_port=8025)
