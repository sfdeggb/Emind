# Emind 项目结构指南

## 概述

Emind 项目已经过重构，采用了更加清晰和模块化的结构。本文档详细说明了新的项目结构和使用方法。

## 项目结构

```
Emind/
├── README.md                    # 项目说明文档
├── requirements.txt             # Python依赖包
├── setup.py                    # 安装配置文件
├── .gitignore                  # Git忽略文件
├── .env.template               # 环境变量模板
├── 
├── emind/                      # 主包目录
│   ├── __init__.py            # 包初始化文件
│   ├── core/                  # 核心模块
│   │   ├── __init__.py
│   │   ├── agent.py          # 主Agent类
│   │   └── config_manager.py # 配置管理
│   │
│   ├── models/                # 模型相关
│   │   ├── __init__.py
│   │   ├── emotion/          # 情感分析
│   │   │   ├── __init__.py
│   │   │   ├── analyzer.py
│   │   │   └── data/         # 情感数据
│   │   └── music/            # 音乐模型
│   │       ├── __init__.py
│   │       └── generators.py
│   │
│   ├── plugins/               # 插件系统
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── registry.py
│   │
│   ├── skills/                # AI技能
│   │   ├── __init__.py
│   │   └── music_agent/
│   │
│   ├── ui/                    # 用户界面
│   │   ├── __init__.py
│   │   ├── web/              # Web界面
│   │   │   ├── __init__.py
│   │   │   ├── server.py
│   │   │   ├── pages/        # 页面组件
│   │   │   └── components/   # UI组件
│   │   └── cli/              # 命令行界面
│   │       ├── __init__.py
│   │       └── interface.py
│   │
│   ├── utils/                 # 工具函数
│   │   ├── __init__.py
│   │   ├── text.py
│   │   ├── audio.py
│   │   └── file.py
│   │
│   └── templates/             # 模板文件
│       ├── __init__.py
│       └── music/
│
├── config/                    # 配置文件
│   ├── default.yaml
│   ├── secure.yaml
│   └── environments/
│
├── tests/                     # 测试文件
│   ├── __init__.py
│   ├── test_core/
│   ├── test_models/
│   └── test_ui/
│
├── scripts/                   # 脚本文件
│   ├── setup.py
│   ├── download_models.py
│   └── migrate.py
│
├── docs/                      # 文档
│   ├── api/
│   ├── guides/
│   └── examples/
│
├── data/                      # 数据文件
│   ├── models/
│   ├── audio/
│   └── cache/
│
└── logs/                      # 日志文件
```

## 核心模块说明

### 1. emind/core/
核心模块包含系统的主要功能：
- `agent.py`: 主Agent类，负责协调所有功能
- `config_manager.py`: 配置管理器，处理API密钥和配置

### 2. emind/models/
模型相关模块：
- `emotion/`: 情感分析模型
- `music/`: 音乐生成和处理模型

### 3. emind/plugins/
插件系统：
- `base.py`: 插件基类
- `registry.py`: 插件注册和管理

### 4. emind/ui/
用户界面：
- `web/`: Web界面（Gradio）
- `cli/`: 命令行界面

### 5. emind/utils/
工具函数：
- `text.py`: 文本处理工具
- `audio.py`: 音频处理工具
- `file.py`: 文件操作工具

## 使用方法

### 1. 安装
```bash
pip install -e .
```

### 2. 配置
```bash
cp .env.template .env
# 编辑 .env 文件，填入API密钥
```

### 3. 命令行使用
```bash
emind "生成一首快乐的歌曲"
emind --check-config
emind --mode gradio --port 8022
```

### 4. Python API使用
```python
from emind import MusicAgent

# 创建Agent实例
agent = MusicAgent("config/default.yaml", mode="cli")

# 运行任务
result = agent.run("生成一首快乐的歌曲")
print(result)
```

## 迁移指南

### 从旧版本迁移

1. **备份数据**：备份现有的配置和数据文件
2. **更新导入**：更新代码中的导入路径
3. **重新配置**：使用新的配置系统
4. **测试功能**：运行测试确保功能正常

### 导入路径变更

| 旧路径 | 新路径 |
|--------|--------|
| `from agent import MusicAgent` | `from emind.core.agent import MusicAgent` |
| `from config_manager import get_secure_config` | `from emind.core.config_manager import get_secure_config` |
| `from emotion.emo_analyse import QEmo` | `from emind.models.emotion.analyzer import EmotionAnalyzer` |

## 开发指南

### 1. 添加新功能
- 在相应的模块目录下创建新文件
- 更新 `__init__.py` 文件
- 添加相应的测试

### 2. 添加新插件
- 继承 `BasePlugin` 类
- 在 `plugins/registry.py` 中注册
- 实现必要的接口方法

### 3. 添加新UI组件
- 在 `ui/web/components/` 下创建组件
- 在 `ui/web/pages/` 下创建页面
- 更新服务器配置

## 测试

运行测试：
```bash
pytest tests/
```

运行特定测试：
```bash
pytest tests/test_core/
pytest tests/test_models/
pytest tests/test_ui/
```

## 部署

### 开发环境
```bash
pip install -e ".[dev]"
emind --mode gradio
```

### 生产环境
```bash
pip install .
emind-server --port 8022
```

## 故障排除

### 常见问题

1. **导入错误**：检查Python路径和包安装
2. **配置错误**：检查配置文件和环境变量
3. **依赖缺失**：运行 `pip install -r requirements.txt`

### 调试模式
```bash
emind --debug "你的输入"
```

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 创建 Pull Request

## 许可证

MIT License
