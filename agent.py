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

from model_utils import lyric_format
from model_utils import rietry_parase_json 
from plugins import get_task_map, init_plugins
from plugins_custom import update_plugins_custom
from ui.shard import gradio
from template.get_default_template import default_lyric_template

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
        self.config = yaml.load(open(config_path, "r"), Loader=yaml.FullLoader)
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
        skills_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "skills")
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
            api_key, org_id = sk.openai_settings_from_dot_env()
            self.kernel.add_text_completion_service("dv", OpenAITextCompletion(self.config["model"], api_key, org_id,
                                                                               endpoint="https://api.aiproxy.io/v1"))
        
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
        
        if len(locals) > 0:
            self.task_context["history"] += f"In this task, <GENERATED>-{command['id']}: {json.dumps(locals)}. "

        return output
    
    #根据输入文本，调用chat_function进行对话
    def skillchat(self, input_text, chat_function, context):
        #try reset the setting
        context["input"] = input_text
        answer = chat_function.invoke(context=context)
        answer = str(answer).strip()
        context["history"] += f"\nuser: {input_text}\nassistant: {answer}\n"

        # Manage history
        context["history"] = ' '.join(context["history"].split()[-self.config["history_len"]:])

        return answer
    
    def fix_depth(self, tasks):
        for task in tasks:
            task["dep"] = list(set(re.findall(r"<GENERATED>-([0-9]+)", json.dumps(task))))
            task["dep"] = [int(d) for d in task["dep"]]#这里task正常来说是一个字典
            if len(task["dep"]) == 0:
                task["dep"] = [-1]
        
        return tasks

    def collect_result(self, command, choose, inference_result):
        result = {"task": command}
        result["inference result"] = inference_result
        result["choose model result"] = choose
        self.logger.debug(f"inference result: {inference_result}")
        return result

    def run_task(self, input_text, command, results):
        if self.error_event.is_set():
            return

        id = command["id"]
        args = command["args"]
        task = command["task"]
        deps = command["dep"]

        if deps[0] != -1:
            dep_tasks = [results[dep] for dep in deps]
        else:
            dep_tasks = []

        self.logger.debug(f"Run task: {id} - {task}")
        self.logger.debug("Deps: " + json.dumps(dep_tasks))

        inst_args = []
        for arg in args:
            for key in arg:
                if isinstance(arg[key], str):
                    if "<GENERATED>" in arg[key]:
                        dep_id = int(arg[key].split("-")[1])
                        for result in results[dep_id]["inference result"]:
                            if key in result:
                                tmp_arg = arg.copy()
                                tmp_arg[key] = result[key]
                                inst_args.append(tmp_arg)
                    else: 
                        tmp_arg = arg.copy()
                        inst_args.append(tmp_arg)

                elif isinstance(arg[key], list):
                    tmp_arg = arg.copy()
                    for t in range(len(tmp_arg[key])):
                        item = tmp_arg[key][t]
                        if "<GENERATED>" in item:
                            dep_id = int(item.split("-")[1])
                            for result in results[dep_id]["inference result"]:
                                if key in result:
                                    tmp_arg[key][t] = result[key]
                                    break
                                    
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
                self.logger.warning(f"no available models on {task} task.")
                inference_result = [{"error": f"{command['task']} not found in available tasks."}]
                results[id] = self.collect_result(command, "", inference_result)
                return False

            candidates = [pipe_id for pipe_id in self.task_map[task] if pipe_id in self.pipes]
            candidates = candidates[:self.config["candidate_tools"]]
            self.logger.debug(f"avaliable models on {command['task']}: {candidates}")

            if len(candidates) == 0:
                self.logger.warning(f"unloaded models on {task} task.")
                inference_result = [{"error": f"models for {command['task']} are not loaded."}]
                results[id] = self.collect_result(command, "", inference_result)
                return False
            
            if len(candidates) == 1:
                best_model_id = candidates[0]
                reason = "Only one model available."
                choose = {"id": best_model_id, "reason": reason}
                self.logger.debug(f"chosen model: {choose}")
            else:
                #self.tool_context["available"] = ', '.join([cand.id for cand in candidates])
                self.tool_context["available"] = ', '.join([cand for cand in candidates])
                choose_str = self.skillchat(input_text, self.tool_selector, self.tool_context)
                self.logger.debug(f"chosen model: {choose_str}")
                choose = json.loads(choose_str)
                reason = choose["reason"]
                best_model_id = choose["id"]

            inference_result = self.model_inference(best_model_id, command, device=self.config["device"])

        results[id] = self.collect_result(command, choose, inference_result)
        for result in inference_result:
            if "error" in result:
                self.error_event.set()
                break
            
        return

    def chat(self, input_text):
        #CLI中调用chat函数
        start = time.time()
        self.logger.info(f"input: {input_text}")

        #调用skillchat函数，进行对话
        task_str = self.skillchat(input_text, self.task_planner, self.task_context)
        self.logger.info(f"plans: {task_str}")
        try:
            tasks = json.loads(task_str)
        except Exception as e:
            self.logger.debug(e)
            
            response = self.skillchat(input_text, self.chatbot, self.chat_context)
            return response, {"0": "Task parsing error, reply using ChatGPT."}
        # tasks=[]
        # try:
        #     tasks = json.loads(task_str)
        # except Exception as e1:
        #     self.logger.debug(e1)
        #     self.logger.debug("第一次直接解析任务失败，正在尝试重新解析")
        #     try:
        #         tasks = rietry_parase_json(task_str)
        #     except Exception as e2:
        #         self.logger.debug(e2)
        #         self.logger.debug("第二次解析任务失败，正在尝试使用ChatGPT进行对话")

        #         response = self.skillchat(input_text, self.chatbot, self.chat_context)
        #         return response, {"0": "Task parsing error, reply using ChatGPT."}
        
        if len(tasks) == 0:
            response = self.skillchat(input_text, self.chatbot, self.chat_context)
            return response, {"0": "No task detected, reply using ChatGPT."}
        
        tasks = self.fix_depth(tasks)
        results = {}
        threads = []
        d = dict()
        retry = 0
        self.error_event = threading.Event()
        while True:
            num_thread = len(threads)
            if self.error_event.is_set():
                break
            for task in tasks:
                # logger.debug(f"d.keys(): {d.keys()}, dep: {dep}")
                for dep_id in task["dep"]:
                    if dep_id >= task["id"]:#如果依赖id大于任务id，说明有问题
                        task["dep"] = [-1]#重置依赖
                        break
                dep = task["dep"]
                if dep[0] == -1 or len(list(set(dep).intersection(d.keys()))) == len(dep):
                    tasks.remove(task)
                    #开始一个线程
                    thread = threading.Thread(target=self.run_task, args=(input_text, task, d))
                    thread.start()
                    threads.append(thread)

            if num_thread == len(threads):
                time.sleep(0.5)
                retry += 1

            if retry > 120:
                self.logger.debug("User has waited too long, Loop break.")
                break

            if len(tasks) == 0:
                break

        for thread in threads:
            thread.join()
        
        results = d.copy()
        self.logger.debug("results: ", results)
        #这里只保留最后的推理结果
        results = {key: results[key] for key in sorted(results.keys())[-1:]}
        #将推理结果转换为字符串，添加到response_context中
        self.response_context["processes"] = str(results)

        response = self.skillchat(input_text, self.responder, self.response_context)
        
        end = time.time()
        during = end - start
        self.logger.info(f"time: {during}s")
        return response, results

    def _update_pipes(self,name,update_conf):
        """更新插件"""
        self.pipes[name]=update_plugins_custom(name,self.config,update_conf)#需要返回一个新对象
        self._init_task_context()#初始化任务上下文
        self._init_tool_context()#初始化工具上下文
    def update_pipes_rec(self,name,update_conf):
        pass
    def _delete_pipes(self,name,plugin_config):
        """删除插件"""
        default_pipes = self.pipes
        if "text_audio_model" in plugin_config :
            text_audio_model = plugin_config["text_audio_model"] 
            #使得模型不可用
            if text_audio_model != "None":
                #self.config["disabled_tools"] = text_audio_model#光做替换可能不会生效哦
                #这里还是需要pipes
                self.pipes.pop("text_audio_model")
        if "music_recommend_model_with_chinese" in plugin_config:
            music_recommend_model_with_chinese = plugin_config["music_recommend_model_with_chinese"]
            if music_recommend_model_with_chinese == 'False':
                #self.config["disabled_tools"] = music_recommend_model_with_chinese
                self.pipes.pop("music_recommand_chinese")
        if "music_recommend_model_with_english" in plugin_config:
            music_recommend_model_with_english = plugin_config["music_recommend_model_with_english"]
            if music_recommend_model_with_english == 'False':
                #self.config["disabled_tools"] = music_recommend_model_with_english
                self.pipes.pop("music_recommand_english")
        if "music_recommend_model_with_english_based_content" in plugin_config:
            music_recommend_model_with_english_based_content = plugin_config["music_recommend_model_with_english_based_content"]
            if music_recommend_model_with_english_based_content == 'False':
                #self.config["disabled_tools"] = music_recommend_model_with_english_based_content
                self.pipes.pop("music_recommand_content")
        #如果插件被删除了，需要重新初始化工具上下文
        if default_pipes != self.pipes:
            self._init_task_context()#初始化任务上下文
            self._init_tool_context()#初始化工具上下文
    
def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="music agent config")
    parser.add_argument("--config", type=str, help="a YAML file path.")

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    #agent = MusicAgent(args.config, mode="cli")
    #设置环境变量
    #openai.base_url="https://one.aiskt.com/v1/chat"
    #openai.api_key="sk-KIRPMVASy9iN8i7GAd67A88f0f8745EdB8D363Eb82305c8b"
    #os.environ["OPENAI_BASE_URL"] = "https://one.aiskt.com/v1/chat" # 注意换成你自己的地址
    os.environ["OPENAI_API_KEY"] = "sk-zn75qYaaBWlYD0MCnmMZeZpnyhMMgosTQSMkMZjD2Yny2OQV"
    
    agent = MusicAgent("config.yaml", mode="cli")
    print("Input exit or quit to stop the agent.")
    while True:
        message = input("User input: ")
        if message in ["exit", "quit"]:
            break

        #print(agent.chat(message))
        messages,result = agent.chat(message)
        print(messages)
        #将任务结果写入文件，查看任务链
        with open("/root/muzic/musicagent/result_11.txt","a+") as f:
            f.write("\n\n")
            f.write(str(result))

    