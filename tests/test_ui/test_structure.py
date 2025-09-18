#!/usr/bin/env python3
"""
Test script for new project structure
"""

import os
import sys
from pathlib import Path

def test_directory_structure():
    """Test if all required directories exist"""
    print("Testing directory structure...")
    
    required_dirs = [
        "emind",
        "emind/core",
        "emind/models",
        "emind/models/emotion",
        "emind/plugins",
        "emind/skills",
        "emind/ui",
        "emind/ui/web",
        "emind/ui/cli",
        "emind/utils",
        "emind/templates",
        "config",
        "tests",
        "scripts",
        "docs",
        "data"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
        else:
            print(f"  ✓ {dir_path}")
    
    if missing_dirs:
        print(f"  ✗ Missing directories: {missing_dirs}")
        return False
    
    print("  ✓ All required directories exist")
    return True

def test_package_files():
    """Test if all package __init__.py files exist"""
    print("\nTesting package files...")
    
    package_dirs = [
        "emind",
        "emind/core",
        "emind/models",
        "emind/models/emotion",
        "emind/plugins",
        "emind/skills",
        "emind/ui",
        "emind/ui/web",
        "emind/ui/cli",
        "emind/utils",
        "emind/templates",
        "tests",
        "tests/test_core",
        "tests/test_models",
        "tests/test_ui"
    ]
    
    missing_files = []
    for package_dir in package_dirs:
        init_file = os.path.join(package_dir, "__init__.py")
        if not os.path.exists(init_file):
            missing_files.append(init_file)
        else:
            print(f"  ✓ {init_file}")
    
    if missing_files:
        print(f"  ✗ Missing __init__.py files: {missing_files}")
        return False
    
    print("  ✓ All package files exist")
    return True

def test_core_files():
    """Test if core files exist"""
    print("\nTesting core files...")
    
    core_files = [
        "emind/core/agent.py",
        "emind/core/config_manager.py",
        "emind/plugins/base.py",
        "emind/plugins/registry.py",
        "emind/utils/text.py",
        "emind/models/emotion/analyzer.py",
        "setup.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in core_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"  ✓ {file_path}")
    
    if missing_files:
        print(f"  ✗ Missing core files: {missing_files}")
        return False
    
    print("  ✓ All core files exist")
    return True

def test_config_files():
    """Test if configuration files exist"""
    print("\nTesting configuration files...")
    
    config_files = [
        "config/default.yaml",
        "config/secure.yaml",
        ".env.template",
        ".gitignore"
    ]
    
    missing_files = []
    for file_path in config_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"  ✓ {file_path}")
    
    if missing_files:
        print(f"  ✗ Missing config files: {missing_files}")
        return False
    
    print("  ✓ All configuration files exist")
    return True

def test_documentation():
    """Test if documentation exists"""
    print("\nTesting documentation...")
    
    doc_files = [
        "docs/guides/PROJECT_STRUCTURE.md",
        "docs/guides/SECURITY_SETUP.md",
        "scripts/migrate.py"
    ]
    
    missing_files = []
    for file_path in doc_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"  ✓ {file_path}")
    
    if missing_files:
        print(f"  ✗ Missing documentation: {missing_files}")
        return False
    
    print("  ✓ All documentation exists")
    return True

def main():
    """Main test function"""
    print("Emind Project Structure Test")
    print("=" * 40)
    
    tests = [
        test_directory_structure,
        test_package_files,
        test_core_files,
        test_config_files,
        test_documentation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"  ✗ Test failed with error: {e}")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! Project structure is correct.")
        return True
    else:
        print("✗ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
