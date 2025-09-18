#!/usr/bin/env python3
"""
Command Line Interface for Emind
"""

import argparse
import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from emind.core.agent import MusicAgent
from emind.core.config_manager import get_secure_config


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Emind - AI Music Recommendation and Generation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  emind --config config/default.yaml "生成一首快乐的歌曲"
  emind --mode gradio --port 8022
  emind --check-config
        """
    )
    
    parser.add_argument(
        "input_text",
        nargs="?",
        help="Input text for music generation or query"
    )
    
    parser.add_argument(
        "--config",
        default="config/default.yaml",
        help="Path to configuration file (default: config/default.yaml)"
    )
    
    parser.add_argument(
        "--mode",
        choices=["cli", "gradio"],
        default="cli",
        help="Operation mode (default: cli)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8022,
        help="Port for web interface (default: 8022)"
    )
    
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Check configuration and API keys"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    try:
        if args.check_config:
            check_configuration(args.config)
            return
        
        if args.mode == "gradio":
            start_web_interface(args.config, args.port, args.debug)
        else:
            if not args.input_text:
                print("Error: Input text is required for CLI mode")
                parser.print_help()
                sys.exit(1)
            run_cli_mode(args.config, args.input_text, args.debug)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)


def check_configuration(config_path):
    """Check configuration and API keys"""
    print("Checking Emind configuration...")
    
    try:
        config_manager = get_secure_config(config_path)
        config_manager.load_env_file()
        
        # Check API keys
        api_keys = config_manager.get_api_keys()
        validation_results = config_manager.validate_api_keys()
        missing_keys = config_manager.get_missing_keys()
        
        print(f"\nConfiguration file: {config_path}")
        print(f"API Keys Status:")
        
        for key, is_valid in validation_results.items():
            status = "✓ Valid" if is_valid else "✗ Missing/Invalid"
            print(f"  {key}: {status}")
        
        if missing_keys:
            print(f"\nMissing API Keys: {', '.join(missing_keys)}")
            print("Please check your .env file or environment variables")
        else:
            print("\n✓ All API keys are configured")
            
    except Exception as e:
        print(f"Configuration check failed: {e}")


def run_cli_mode(config_path, input_text, debug):
    """Run in CLI mode"""
    print(f"Initializing Emind with config: {config_path}")
    
    agent = MusicAgent(config_path, mode="cli")
    
    print(f"Processing: {input_text}")
    result = agent.run(input_text)
    
    if result:
        if "response" in result:
            print(f"\nResponse: {result['response']}")
        if "results" in result:
            print(f"\nResults: {len(result['results'])} tasks completed")
    else:
        print("No result generated")


def start_web_interface(config_path, port, debug):
    """Start web interface"""
    print(f"Starting Emind web interface on port {port}")
    
    try:
        from emind.ui.web.server import main as web_main
        web_main(config_path, port, debug)
    except ImportError:
        print("Web interface not available. Please install required dependencies.")
        sys.exit(1)


if __name__ == "__main__":
    main()
