#!/usr/bin/env python3
"""
Test script for modern UI components
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_ui_components():
    """Test UI components"""
    print("Testing Modern UI Components...")
    
    try:
        # Test CSS file
        css_path = "emind/ui/web/components/styles/modern_theme.css"
        if os.path.exists(css_path):
            print(f"✓ CSS file exists: {css_path}")
            with open(css_path, 'r') as f:
                css_content = f.read()
                if "emind-header" in css_content and "emind-card" in css_content:
                    print("✓ CSS contains required classes")
                else:
                    print("✗ CSS missing required classes")
        else:
            print(f"✗ CSS file not found: {css_path}")
        
        # Test component files
        component_files = [
            "emind/ui/web/components/modern_components.py",
            "emind/ui/web/pages/modern_index.py",
            "emind/ui/web/pages/modern_chat.py",
            "emind/ui/web/pages/modern_settings.py",
            "emind/ui/web/server.py"
        ]
        
        for file_path in component_files:
            if os.path.exists(file_path):
                print(f"✓ Component file exists: {file_path}")
            else:
                print(f"✗ Component file not found: {file_path}")
        
        # Test imports
        try:
            from emind.ui.web.components.modern_components import ModernUIComponents
            print("✓ ModernUIComponents import successful")
        except ImportError as e:
            print(f"✗ ModernUIComponents import failed: {e}")
        
        try:
            from emind.ui.web.pages.modern_index import create_modern_index_ui
            print("✓ Modern index import successful")
        except ImportError as e:
            print(f"✗ Modern index import failed: {e}")
        
        try:
            from emind.ui.web.pages.modern_chat import ModernChatInterface
            print("✓ Modern chat import successful")
        except ImportError as e:
            print(f"✗ Modern chat import failed: {e}")
        
        try:
            from emind.ui.web.pages.modern_settings import create_modern_settings_ui
            print("✓ Modern settings import successful")
        except ImportError as e:
            print(f"✗ Modern settings import failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        return False

def test_ui_demo():
    """Test UI demo creation"""
    print("\nTesting UI Demo Creation...")
    
    try:
        # Test index demo
        from emind.ui.web.pages.modern_index import create_modern_index_demo
        print("✓ Index demo creation successful")
        
        # Test chat demo
        from emind.ui.web.pages.modern_chat import create_modern_chat_demo
        print("✓ Chat demo creation successful")
        
        # Test settings demo
        from emind.ui.web.pages.modern_settings import create_modern_settings_demo
        print("✓ Settings demo creation successful")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🎨 EMIND Modern UI Test")
    print("=" * 40)
    
    # Test components
    components_ok = test_ui_components()
    
    # Test demos
    demos_ok = test_ui_demo()
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"Components: {'✓ PASS' if components_ok else '✗ FAIL'}")
    print(f"Demos: {'✓ PASS' if demos_ok else '✗ FAIL'}")
    
    if components_ok and demos_ok:
        print("\n🎉 All tests passed! Modern UI is ready.")
        print("\nTo run the demos:")
        print("  python emind/ui/web/pages/modern_index.py")
        print("  python emind/ui/web/pages/modern_chat.py")
        print("  python emind/ui/web/pages/modern_settings.py")
        print("  python emind/ui/web/server.py")
        return True
    else:
        print("\n❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
