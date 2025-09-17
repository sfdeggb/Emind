"""
安全的配置管理模块
用于管理API密钥和其他敏感配置信息
"""

import os
import yaml
import logging
from typing import Dict, Any, Optional
from pathlib import Path


class SecureConfigManager:
    """安全的配置管理器"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.logger = logging.getLogger(__name__)
        self._config = None
        self._load_config()
    
    def _load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f)
        except FileNotFoundError:
            self.logger.error(f"配置文件 {self.config_path} 未找到")
            raise
        except yaml.YAMLError as e:
            self.logger.error(f"配置文件解析错误: {e}")
            raise
    
    def get_config(self) -> Dict[str, Any]:
        """获取完整配置"""
        return self._config.copy()
    
    def get_api_keys(self) -> Dict[str, str]:
        """安全地获取API密钥，优先从环境变量读取"""
        api_keys = {}
        
        # HuggingFace Token
        api_keys['huggingface_token'] = os.getenv(
            'HUGGINGFACE_TOKEN', 
            self._config.get('huggingface', {}).get('token', '')
        )
        
        # Spotify API Keys
        api_keys['spotify_client_id'] = os.getenv(
            'SPOTIFY_CLIENT_ID',
            self._config.get('spotify', {}).get('client_id', '')
        )
        api_keys['spotify_client_secret'] = os.getenv(
            'SPOTIFY_CLIENT_SECRET',
            self._config.get('spotify', {}).get('client_secret', '')
        )
        api_keys['spotify_access_token'] = os.getenv(
            'SPOTIFY_ACCESS_TOKEN',
            self._config.get('spotify', {}).get('access_token', '')
        )
        
        # Google API Keys
        api_keys['google_api_key'] = os.getenv(
            'GOOGLE_API_KEY',
            self._config.get('google', {}).get('api_key', '')
        )
        api_keys['google_custom_search_engine_id'] = os.getenv(
            'GOOGLE_CUSTOM_SEARCH_ENGINE_ID',
            self._config.get('google', {}).get('custom_search_engine_id', '')
        )
        
        # OpenAI API Key
        api_keys['openai_api_key'] = os.getenv('OPENAI_API_KEY', '')
        
        return api_keys
    
    def validate_api_keys(self) -> Dict[str, bool]:
        """验证API密钥是否有效"""
        api_keys = self.get_api_keys()
        validation_results = {}
        
        for key_name, key_value in api_keys.items():
            if key_value:
                # 基本格式验证
                if key_name == 'huggingface_token' and key_value.startswith('hf_'):
                    validation_results[key_name] = True
                elif key_name == 'openai_api_key' and key_value.startswith('sk-'):
                    validation_results[key_name] = True
                elif key_name in ['spotify_client_id', 'spotify_client_secret', 'google_api_key']:
                    validation_results[key_name] = len(key_value) > 10
                else:
                    validation_results[key_name] = len(key_value) > 0
            else:
                validation_results[key_name] = False
        
        return validation_results
    
    def get_missing_keys(self) -> list:
        """获取缺失的API密钥列表"""
        validation_results = self.validate_api_keys()
        return [key for key, is_valid in validation_results.items() if not is_valid]
    
    def create_env_template(self, output_path: str = ".env.template"):
        """创建环境变量模板文件"""
        template_content = """# Emind API Keys Configuration
# 复制此文件为 .env 并填入您的API密钥

# HuggingFace Token (用于模型下载)
HUGGINGFACE_TOKEN=your_huggingface_token_here

# Spotify API Keys (用于音乐推荐和搜索)
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
SPOTIFY_ACCESS_TOKEN=your_spotify_access_token_here

# Google API Keys (用于网络搜索)
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CUSTOM_SEARCH_ENGINE_ID=your_google_custom_search_engine_id_here

# OpenAI API Key (用于LLM功能)
OPENAI_API_KEY=your_openai_api_key_here
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        self.logger.info(f"环境变量模板已创建: {output_path}")
    
    def load_env_file(self, env_path: str = ".env"):
        """加载.env文件中的环境变量"""
        if os.path.exists(env_path):
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()
            self.logger.info(f"已加载环境变量文件: {env_path}")
        else:
            self.logger.warning(f"环境变量文件不存在: {env_path}")


def get_secure_config(config_path: str = "config.yaml") -> SecureConfigManager:
    """获取安全配置管理器的实例"""
    return SecureConfigManager(config_path)
