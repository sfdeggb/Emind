"""
Text processing utilities
"""

import re
import json


def lyric_format(text):
    """Format lyrics from model output"""
    # Remove common prefixes and clean up the text
    prefixes_to_remove = [
        "歌词：", "歌词:", "Lyrics:", "lyrics:", 
        "以下是歌词：", "以下是歌词:", "Here are the lyrics:",
        "歌词内容：", "歌词内容:", "Lyric content:"
    ]
    
    for prefix in prefixes_to_remove:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    
    # Remove extra whitespace and newlines
    text = re.sub(r'\n+', '\n', text)
    text = text.strip()
    
    return text


def rietry_parase_json(text, max_retries=3):
    """Parse JSON with retry mechanism"""
    for attempt in range(max_retries):
        try:
            # Try to find JSON in the text
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                return json.loads(json_str)
            else:
                return json.loads(text)
        except json.JSONDecodeError as e:
            if attempt == max_retries - 1:
                raise e
            # Try to fix common JSON issues
            text = text.replace("'", '"')  # Replace single quotes with double quotes
            text = re.sub(r'(\w+):', r'"\1":', text)  # Add quotes around keys
    
    return None


def clean_text(text):
    """Clean and normalize text input"""
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters that might cause issues
    text = re.sub(r'[^\w\s\u4e00-\u9fff.,!?;:()]', '', text)
    
    return text.strip()


def extract_keywords(text, max_keywords=10):
    """Extract keywords from text"""
    # Simple keyword extraction based on word frequency
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
        'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 
        'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
        '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个'
    }
    
    # Count word frequency
    word_count = {}
    for word in words:
        if word not in stop_words and len(word) > 1:
            word_count[word] = word_count.get(word, 0) + 1
    
    # Return top keywords
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return [word for word, count in sorted_words[:max_keywords]]
