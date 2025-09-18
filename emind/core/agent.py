""" Agent for CLI or APPs"""

import io
import os
import sys
import time
import re
import json
import logging
import yaml
import threading
import argparse
import pdb
import openai 

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion, OpenAITextCompletion

# Updated imports for new structure
from ..utils.text import lyric_format
from ..utils.text import rietry_parase_json 
from ..plugins.registry import get_task_map, init_plugins
from ..plugins.registry import update_plugins_custom
from ..ui.web.components.shard import gradio
from ..templates.music.get_default_template import default_lyric_template
from .config_manager import get_secure_config

class MusicAgent:
    """
    Attributes:
        config_path: A path to a YAML file, referring to the example config.yaml
        mode: Supports "cli" or "gradio", determining when to load the LLM backend.
    """
    def __init__(
            self,
            config_path: str,
            mode: str = "cli",
            ):
        """
        初始化music Agent
        """
        # 使用安全的配置管理器
        self.config_manager = get_secure_config(config_path)
        self.config_manager.load_env_file()  # 加载.env文件
        
        # 获取配置
        self.config = self.config_manager.get_config()
        self.api_keys = self.config_manager.get_api_keys()
        
        # 验证API密钥
        missing_keys = self.config_manager.get_missing_keys()
        if missing_keys:
            self.logger.warning(f"以下API密钥缺失或无效: {', '.join(missing_keys)}")
            self.logger.info("请检查.env文件或环境变量配置")
        
        os.makedirs("logs", exist_ok=True)
        self.src_fold = self.config["src_fold"]
        os.makedirs(self.src_fold, exist_ok=True)

        self._init_logger()
        self.kernel = sk.Kernel()

        self.task_map = get_task_map()
        self.pipes = init_plugins(self.config)

        if mode == "cli":
            self._init_backend_from_env()
        

    def _init_logger(self):
        """
        初始化logger 日志记录器
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        if not self.config["debug"]:
            handler.setLevel(logging.CRITICAL)
        self.logger.addHandler(handler)

        log_file = self.config["log_file"]
        if log_file:
            filehandler = logging.FileHandler(log_file)
            filehandler.setLevel(logging.DEBUG)
            filehandler.setFormatter(formatter)
            self.logger.addHandler(filehandler)

    def _init_semantic_kernel(self):
        """"初始化轻量级的semantic kernel"""
        skills_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "skills")
        pilot_funcs = self.kernel.import_semantic_skill_from_directory(skills_directory, "MusicAgent")
        
        # task planning
        self.task_planner = pilot_funcs["TaskPlanner"]
        self.task_context = self.kernel.create_new_context()
        self.task_context["history"] = ""

        # model selection
        self.tool_selector = pilot_funcs["ToolSelector"]
        self.tool_context = self.kernel.create_new_context()
        self.tool_context["history"] = ""
        self.tool_context["tools"] = ""

        # response
        self.responder = pilot_funcs["Responder"]
        self.response_context = self.kernel.create_new_context()
        self.response_context["history"] = ""
        self.response_context["processes"] = ""

        # chat
        self.chatbot = pilot_funcs["ChatBot"]
        self.chat_context = self.kernel.create_new_context()
        self.chat_context["history"] = ""

    def clear_history(self):
        self.task_context["history"] = ""
        self.tool_context["history"] = ""
        self.response_context["history"] = ""
        self.chat_context["history"] = ""

    def _init_backend_from_env(self):
        """"初始化backend，从环境变量中读取配置"""
        # Configure AI service used by the kernel
        if self.config["use_azure_openai"]:
            deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
            self.kernel.add_text_completion_service("dv", AzureTextCompletion(deployment, endpoint, api_key))
        else:
            # 优先使用环境变量中的OpenAI API Key
            openai_api_key = self.api_keys.get('openai_api_key', '')
            if not openai_api_key:
                # 回退到从环境变量读取
                api_key, org_id = sk.openai_settings_from_dot_env()
            else:
                api_key = openai_api_key
                org_id = ""
            
            self.kernel.add_text_completion_service("dv", OpenAITextCompletion(
                self.config["model"], api_key, org_id,
                endpoint="https://api.aiproxy.io/v1"
            ))
        
        self._init_semantic_kernel()
        self._init_task_context()
        self._init_tool_context()
        
    #根据输入的api_key，初始化backend(在Gradio中使用)
    def _init_backend_from_input(self, api_key):
        # Only OpenAI api is supported in Gradio demo
        self.kernel.add_text_completion_service("dv", OpenAITextCompletion(self.config["model"], api_key, ""))
        
        self._init_semantic_kernel()
        self._init_task_context()
        self._init_tool_context()

    def _init_task_context(self):
        self.task_context["tasks"] = json.dumps(list(self.task_map.keys()))

    def _init_tool_context(self):
        self.tool_context["tools"] = json.dumps(
            [{"id": pipe.id, "attr": pipe.get_attributes()} for pipe in self.pipes.values()]
        )

    def update_tool_attributes(self, pipe_id, **kwargs):
        self.pipes[pipe_id].update_attributes(kwargs)
        self._init_tool_context()

    def model_inference(self, model_id, command, device="cpu"):
        output = self.pipes[model_id].inference(command["args"], command["task"], device)
        
        locals = []
        for result in output:
            if "audio" in result or "sheet_music" in result:
                locals.append(result)
        return locals

    def skillchat(self, input_text, skill, context):
        """与技能进行对话"""
        context["input"] = input_text
        response = skill.invoke(context=context)
        return str(response)

    def collect_result(self, command, choose, inference_result):
        """收集推理结果"""
        result = {"command": command, "choose": choose, "inference_result": inference_result}
        return result

    def run_task(self, input_text, command, results):
        
        task = command["task"]
        inst_args = []
        for arg in command["args"]:
            tmp_arg = {}
            for key, value in arg.items():
                if isinstance(value, str) and value.startswith("<GENERATED>-"):
                    dep_id = int(value.split("-")[-1])
                    if dep_id in results:
                        dep_result = results[dep_id]
                        if "inference_result" in dep_result:
                            for res in dep_result["inference_result"]:
                                if key in res:
                                    tmp_arg[key] = res[key]
                                    break
                        else:
                            tmp_arg[key] = value
                    else:
                        tmp_arg[key] = value
                else:
                    tmp_arg[key] = value
                                    
            inst_args.append(tmp_arg)

        for arg in inst_args:
            for resource in ["audio", "sheet_music"]:
                if resource in arg:
                    if not arg[resource].startswith(self.config["src_fold"]) and not arg[resource].startswith("http") and len(arg[resource]) > 0:
                        arg[resource] = f"{self.config['src_fold']}/{arg[resource]}"

        command["args"] = inst_args

        self.logger.debug(f"parsed task: {command}")

        if task in ["lyric-generation"]: # ChatGPT Can do
            best_model_id = "ChatGPT"
            reason = "ChatGPT performs well on some NLP tasks as well."
            choose = {"id": best_model_id, "reason": reason}
            inference_result = []

            for arg in command["args"]:
                #这里需要生成歌词的长度，保证歌曲旋律的正常生成
                chat_input = f"[{input_text}] contains a task in JSON format {command}. Now you are a {command['task']} system, the arguments are {arg}. Just help me do {command['task']} and give me the result without any additional description.You need to directly give me the lyrics results, no additional information is required."
                response = self.skillchat(chat_input, self.chatbot, self.chat_context)
                #这里将指令模型生成的部分非歌词信息去掉
                try:
                    lyric = lyric_format(response)
                    lyric_content = lyric[4:]
                except:
                    lyric_content = default_lyric_template()
                
                #inference_result.append({"lyric":lyric_format(response)})
                inference_result.append({"lyric":lyric_content})

        else:
            if task not in self.task_map:
                self.logger.error(f"Unknown task: {task}")
                return None
            
            # 使用工具选择器选择最佳模型
            tool_input = f"Task: {task}, Available tools: {json.dumps([{'id': pipe.id, 'attr': pipe.get_attributes()} for pipe in self.pipes.values()])}"
            choose_response = self.skillchat(tool_input, self.tool_selector, self.tool_context)
            
            try:
                choose = json.loads(choose_response)
            except:
                choose = {"id": list(self.pipes.keys())[0], "reason": "Default selection"}
            
            # 执行模型推理
            inference_result = self.model_inference(choose["id"], command, self.config["device"])

        return self.collect_result(command, choose, inference_result)

    def run(self, input_text):
        """运行主要逻辑"""
        # 任务规划
        task_response = self.skillchat(input_text, self.task_planner, self.task_context)
        
        try:
            tasks = json.loads(task_response)
        except:
            self.logger.error("Failed to parse task response")
            return None
        
        if not tasks:
            # 直接聊天
            response = self.skillchat(input_text, self.chatbot, self.chat_context)
            return {"response": response}
        
        # 执行任务
        results = {}
        for task in tasks:
            task_id = task["id"]
            results[task_id] = self.run_task(input_text, task, results)
        
        # 生成响应
        process_text = json.dumps([{"task": r["command"]["task"], "result": r["inference_result"]} for r in results.values() if r])
        response = self.skillchat(process_text, self.responder, self.response_context)
        
        return {"response": response, "results": results}

    def _delete_pipes(self,name,plugin_config):
        """删除管道"""
        if name in self.pipes:
            del self.pipes[name]
            self._init_tool_context()

    def _add_pipes(self,name,plugin_config):
        """添加管道"""
        from ..plugins.registry import init_plugin
        self.pipes[name] = init_plugin(plugin_config, self.config)
        self._init_tool_context()

    def update_plugins(self, plugin_configs):
        """更新插件配置"""
        update_plugins_custom(self.pipes, plugin_configs, self.config)
        self._init_tool_context()

    def get_api_status(self):
        """获取API密钥状态"""
        return {
            "validation_results": self.config_manager.validate_api_keys(),
            "missing_keys": self.config_manager.get_missing_keys()
        }

    def create_env_template(self, output_path: str = ".env.template"):
        """创建环境变量模板"""
        self.config_manager.create_env_template(output_path)
