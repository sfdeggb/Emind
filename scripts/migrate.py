#!/usr/bin/env python3
"""
Migration script for Emind project structure
"""

import os
import shutil
import sys
from pathlib import Path


def backup_old_files():
    """Backup old files before migration"""
    backup_dir = Path("backup_old_structure")
    backup_dir.mkdir(exist_ok=True)
    
    old_files = [
        "agent.py",
        "agent_backup.py", 
        "gradio_agent.py",
        "config.yaml",
        "count.py"
    ]
    
    old_dirs = [
        "ui",
        "emotion", 
        "skills",
        "template",
        "public",
        "auxiliary",
        "reFdemo"
    ]
    
    print("Backing up old files...")
    
    for file in old_files:
        if os.path.exists(file):
            shutil.copy2(file, backup_dir / file)
            print(f"  Backed up: {file}")
    
    for dir_name in old_dirs:
        if os.path.exists(dir_name):
            shutil.copytree(dir_name, backup_dir / dir_name, dirs_exist_ok=True)
            print(f"  Backed up: {dir_name}/")
    
    print(f"Backup completed in: {backup_dir}")


def create_symlinks():
    """Create symlinks for backward compatibility"""
    print("Creating backward compatibility symlinks...")
    
    # Create symlinks for main entry points
    symlinks = {
        "agent.py": "emind/core/agent.py",
        "config_manager.py": "emind/core/config_manager.py",
        "config.yaml": "config/default.yaml"
    }
    
    for link_name, target in symlinks.items():
        if os.path.exists(target) and not os.path.exists(link_name):
            try:
                os.symlink(target, link_name)
                print(f"  Created symlink: {link_name} -> {target}")
            except OSError as e:
                print(f"  Failed to create symlink {link_name}: {e}")


def update_imports_in_file(file_path):
    """Update imports in a Python file"""
    if not file_path.endswith('.py'):
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update common imports
        import_mappings = {
            'from agent import': 'from emind.core.agent import',
            'from config_manager import': 'from emind.core.config_manager import',
            'from emotion.emo_analyse import': 'from emind.models.emotion.analyzer import',
            'from plugins import': 'from emind.plugins.registry import',
            'from template.get_default_template import': 'from emind.templates.music.get_default_template import',
            'from ui.shard import': 'from emind.ui.web.components.shard import',
        }
        
        updated = False
        for old_import, new_import in import_mappings.items():
            if old_import in content:
                content = content.replace(old_import, new_import)
                updated = True
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Updated imports in: {file_path}")
    
    except Exception as e:
        print(f"  Error updating {file_path}: {e}")


def update_imports():
    """Update imports in all Python files"""
    print("Updating imports in Python files...")
    
    # Find all Python files
    for root, dirs, files in os.walk('.'):
        # Skip certain directories
        if any(skip in root for skip in ['.git', '__pycache__', 'backup_old_structure']):
            continue
        
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                update_imports_in_file(file_path)


def main():
    """Main migration function"""
    print("Emind Project Structure Migration")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--backup-only':
        backup_old_files()
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == '--update-imports':
        update_imports()
        return
    
    if len(sys.argv) > 1 and sys.argv[1] == '--symlinks':
        create_symlinks()
        return
    
    # Full migration
    print("Starting full migration...")
    
    # Step 1: Backup old files
    backup_old_files()
    
    # Step 2: Update imports
    update_imports()
    
    # Step 3: Create symlinks
    create_symlinks()
    
    print("\nMigration completed!")
    print("\nNext steps:")
    print("1. Test the new structure: python -m emind.ui.cli.interface --check-config")
    print("2. Update your scripts to use new import paths")
    print("3. Remove old files if everything works correctly")
    print("4. Run tests: pytest tests/")


if __name__ == "__main__":
    main()
