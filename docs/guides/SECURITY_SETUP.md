# Emind 安全配置指南

## 概述

为了提高系统安全性，Emind现在使用环境变量来管理敏感的API密钥，而不是直接在配置文件中存储。

## 配置步骤

### 1. 环境变量配置

1. 复制环境变量模板文件：
   ```bash
   cp .env.template .env
   ```

2. 编辑 `.env` 文件，填入您的API密钥：
   ```bash
   # HuggingFace Token (用于模型下载)
   HUGGINGFACE_TOKEN=your_actual_huggingface_token
   
   # Spotify API Keys (用于音乐推荐和搜索)
   SPOTIFY_CLIENT_ID=your_actual_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_actual_spotify_client_secret
   SPOTIFY_ACCESS_TOKEN=your_actual_spotify_access_token
   
   # Google API Keys (用于网络搜索)
   GOOGLE_API_KEY=your_actual_google_api_key
   GOOGLE_CUSTOM_SEARCH_ENGINE_ID=your_actual_google_custom_search_engine_id
   
   # OpenAI API Key (用于LLM功能)
   OPENAI_API_KEY=your_actual_openai_api_key
   ```

### 2. 使用安全配置

现在您可以使用 `config_secure.yaml` 作为配置文件，它不包含任何敏感信息：

```python
from agent_updated import MusicAgent

# 使用安全配置
agent = MusicAgent("config_secure.yaml", mode="cli")

# 检查API密钥状态
status = agent.get_api_status()
print("API密钥状态:", status)
```

### 3. 验证配置

系统会自动验证API密钥的有效性，并在日志中报告缺失或无效的密钥。

## 安全特性

1. **环境变量优先**：系统优先从环境变量读取API密钥
2. **配置验证**：自动验证API密钥格式和有效性
3. **敏感信息保护**：配置文件不再包含敏感信息
4. **Git安全**：`.env` 文件已添加到 `.gitignore`，不会被提交到版本控制

## 迁移指南

如果您正在从旧版本迁移：

1. 备份您的 `config.yaml` 文件
2. 从旧配置中提取API密钥
3. 将密钥添加到 `.env` 文件
4. 使用 `config_secure.yaml` 替换 `config.yaml`
5. 更新代码以使用 `agent_updated.py`

## 故障排除

### 常见问题

1. **API密钥未找到**：确保 `.env` 文件存在且包含正确的密钥
2. **权限错误**：确保 `.env` 文件有正确的读取权限
3. **格式错误**：确保API密钥格式正确（如OpenAI密钥以'sk-'开头）

### 调试

启用调试模式以获取更多信息：
```yaml
# 在 config_secure.yaml 中
debug: true
```

## 最佳实践

1. 定期轮换API密钥
2. 使用最小权限原则
3. 监控API使用情况
4. 不要在代码中硬编码密钥
5. 使用不同的密钥用于不同环境（开发、测试、生产）
