#!/usr/bin/env python3
"""
EMIND 现代化UI测试脚本
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_components():
    """测试组件导入"""
    print("🧪 测试组件导入...")
    
    try:
        from emind.ui.web.components.modern_components import ModernUIComponents, ModernLayout
        print("✅ 现代化组件导入成功")
        
        # 测试组件方法
        components = [
            'create_header', 'create_feature_card', 'create_audio_player',
            'create_loading_spinner', 'create_progress_bar', 'create_message_bubble',
            'create_feature_grid', 'create_theme_toggle', 'create_stats_dashboard',
            'create_notification', 'create_quick_action_button', 'create_emotion_indicator'
        ]
        
        for component in components:
            if hasattr(ModernUIComponents, component):
                print(f"  ✅ {component}")
            else:
                print(f"  ❌ {component}")
        
        return True
    except Exception as e:
        print(f"❌ 组件导入失败: {e}")
        return False

def test_pages():
    """测试页面导入"""
    print("\n🧪 测试页面导入...")
    
    try:
        from emind.ui.web.pages.modern_index import create_modern_index_ui
        print("✅ 现代化首页导入成功")
        
        from emind.ui.web.pages.modern_chat import ModernChatInterface
        print("✅ 现代化聊天界面导入成功")
        
        from emind.ui.web.pages.modern_settings import create_modern_settings_ui
        print("✅ 现代化设置页面导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 页面导入失败: {e}")
        return False

def test_server():
    """测试服务器导入"""
    print("\n🧪 测试服务器导入...")
    
    try:
        from emind.ui.web.server import create_modern_emind_app
        print("✅ 基础服务器导入成功")
        
        from emind.ui.web.server_integrated import create_modern_emind_app as create_integrated_app
        print("✅ 集成服务器导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 服务器导入失败: {e}")
        return False

def test_css():
    """测试CSS文件"""
    print("\n🧪 测试CSS文件...")
    
    css_path = "emind/ui/web/components/styles/modern_theme.css"
    if os.path.exists(css_path):
        print("✅ CSS文件存在")
        
        # 检查文件大小
        file_size = os.path.getsize(css_path)
        print(f"  📁 文件大小: {file_size} 字节")
        
        # 检查关键样式
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        key_styles = [
            ':root', '--primary-color', '--bg-primary', '--text-primary',
            '.emind-header', '.emind-card', '.emind-btn', '.emind-input'
        ]
        
        for style in key_styles:
            if style in content:
                print(f"  ✅ {style}")
            else:
                print(f"  ❌ {style}")
        
        return True
    else:
        print("❌ CSS文件不存在")
        return False

def main():
    """主测试函数"""
    print("🎧 EMIND 现代化UI测试")
    print("=" * 50)
    
    tests = [
        test_components,
        test_pages,
        test_server,
        test_css
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！现代化UI系统已准备就绪。")
        print("\n🚀 启动命令:")
        print("  python start_modern_ui.py --mode demo --port 8022")
        print("  python start_modern_ui.py --mode integrated --port 8022")
    else:
        print("❌ 部分测试失败，请检查错误信息。")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
