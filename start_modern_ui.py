#!/usr/bin/env python3
"""
EMIND 现代化UI启动脚本
"""

import os
import sys
import argparse
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="EMIND现代化UI启动器")
    parser.add_argument("--config", default="config/default.yaml", help="配置文件路径")
    parser.add_argument("--port", type=int, default=8022, help="服务器端口")
    parser.add_argument("--debug", action="store_true", help="启用调试模式")
    parser.add_argument("--mode", choices=["demo", "integrated"], default="integrated", help="运行模式")
    
    args = parser.parse_args()
    
    print("🎧 EMIND 现代化UI启动器")
    print("=" * 50)
    print(f"📁 配置文件: {args.config}")
    print(f"🌐 端口: {args.port}")
    print(f"🐛 调试模式: {args.debug}")
    print(f"🔧 运行模式: {args.mode}")
    print("=" * 50)
    
    if args.mode == "demo":
        # 演示模式
        print("🚀 启动演示模式...")
        from emind.ui.web.server import main as demo_main
        demo_main(args.config, args.port, args.debug)
    else:
        # 集成模式
        print("🚀 启动集成模式...")
        from emind.ui.web.server_integrated import main as integrated_main
        integrated_main(args.config, args.port, args.debug)

if __name__ == "__main__":
    main()
