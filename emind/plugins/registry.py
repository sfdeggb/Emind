"""
Plugin registry and management system
"""

import os
import importlib
import logging
from typing import Dict, Any, List
from .base import BasePlugin


class PluginRegistry:
    """Plugin registry for managing all plugins"""
    
    def __init__(self):
        self.plugins = {}
        self.logger = logging.getLogger(__name__)
    
    def register_plugin(self, plugin_id: str, plugin_class):
        """Register a plugin"""
        self.plugins[plugin_id] = plugin_class
        self.logger.info(f"Registered plugin: {plugin_id}")
    
    def get_plugin(self, plugin_id: str):
        """Get a plugin by ID"""
        return self.plugins.get(plugin_id)
    
    def list_plugins(self):
        """List all registered plugins"""
        return list(self.plugins.keys())
    
    def load_plugins_from_directory(self, directory: str):
        """Load plugins from a directory"""
        if not os.path.exists(directory):
            self.logger.warning(f"Plugin directory not found: {directory}")
            return
        
        for filename in os.listdir(directory):
            if filename.endswith('.py') and not filename.startswith('_'):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f"{directory}.{module_name}")
                    if hasattr(module, 'PLUGIN_CLASS'):
                        plugin_class = getattr(module, 'PLUGIN_CLASS')
                        plugin_id = getattr(module, 'PLUGIN_ID', module_name)
                        self.register_plugin(plugin_id, plugin_class)
                except Exception as e:
                    self.logger.error(f"Failed to load plugin {module_name}: {e}")


# Global plugin registry
_plugin_registry = PluginRegistry()


def get_task_map() -> Dict[str, Any]:
    """Get task mapping for plugins"""
    # This would be populated by actual plugins
    return {
        "lyric-generation": "ChatGPT",
        "lyric-to-melody": "MUZIC",
        "lyric-to-audio": "DiffSinger",
        "separate-track": "Spleeter",
        "score-transcription": "PianoTranscription",
        "lyric-recognition": "Whisper",
        "timbre-transfer": "DDSP",
        "audio-mixing": "AudioMixing",
        "music_recommand_Chinese": "MusicRecommendation",
        "music_recommand_english": "MusicRecommendation",
        "web-search": "WebSearch",
        "artist-search": "SpotifyAPI",
        "track-search": "SpotifyAPI",
        "playlist-search": "SpotifyAPI",
    }


def init_plugins(config: Dict[str, Any]) -> Dict[str, BasePlugin]:
    """Initialize all plugins"""
    pipes = {}
    
    # Initialize each plugin based on configuration
    for task, model_id in get_task_map().items():
        try:
            # Create a mock plugin for now
            # In a real implementation, this would create actual plugin instances
            plugin = MockPlugin(task, model_id, config)
            pipes[task] = plugin
        except Exception as e:
            logging.error(f"Failed to initialize plugin {task}: {e}")
    
    return pipes


def update_plugins_custom(pipes: Dict[str, BasePlugin], plugin_configs: Dict[str, Any], config: Dict[str, Any]):
    """Update plugin configurations"""
    for plugin_id, plugin_config in plugin_configs.items():
        if plugin_id in pipes:
            try:
                pipes[plugin_id].update_attributes(plugin_config)
            except Exception as e:
                logging.error(f"Failed to update plugin {plugin_id}: {e}")


class MockPlugin(BasePlugin):
    """Mock plugin for testing purposes"""
    
    def __init__(self, task: str, model_id: str, config: Dict[str, Any]):
        self.id = task
        self.model_id = model_id
        self.config = config
        self.attributes = {}
    
    def get_attributes(self):
        """Get plugin attributes"""
        return self.attributes
    
    def update_attributes(self, attributes: Dict[str, Any]):
        """Update plugin attributes"""
        self.attributes.update(attributes)
    
    def inference(self, args: List[Dict[str, Any]], task: str, device: str = "cpu"):
        """Run inference"""
        # Mock inference result
        return [{"result": f"Mock result for {task} with args {args}"}]
