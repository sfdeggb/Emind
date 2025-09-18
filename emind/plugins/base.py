"""
Base plugin class for Emind plugins
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BasePlugin(ABC):
    """Base class for all Emind plugins"""
    
    def __init__(self, plugin_id: str, config: Dict[str, Any]):
        self.id = plugin_id
        self.config = config
        self.attributes = {}
    
    @abstractmethod
    def get_attributes(self) -> Dict[str, Any]:
        """Get plugin attributes"""
        pass
    
    @abstractmethod
    def update_attributes(self, attributes: Dict[str, Any]):
        """Update plugin attributes"""
        pass
    
    @abstractmethod
    def inference(self, args: List[Dict[str, Any]], task: str, device: str = "cpu") -> List[Dict[str, Any]]:
        """Run inference with given arguments"""
        pass
    
    def validate_args(self, args: List[Dict[str, Any]]) -> bool:
        """Validate input arguments"""
        return True
    
    def get_info(self) -> Dict[str, Any]:
        """Get plugin information"""
        return {
            "id": self.id,
            "attributes": self.get_attributes(),
            "config": self.config
        }
