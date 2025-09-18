"""
Emind - AI Music Recommendation and Generation System

A comprehensive AI-powered music system that provides:
- Music generation from text and lyrics
- Emotion-based music recommendation
- Audio processing and analysis
- Multi-modal music interaction
"""

__version__ = "1.0.0"
__author__ = "Emind Team"
__email__ = "emind@example.com"

# Import main components
from .core.agent import MusicAgent
from .core.config_manager import get_secure_config

# Import submodules
from . import models
from . import ui
from . import utils

__all__ = [
    "MusicAgent",
    "get_secure_config",
    "models",
    "ui", 
    "utils",
]
