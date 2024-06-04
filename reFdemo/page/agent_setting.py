import os 
import sys 
sys.path.append('/root/muzic/musicagent/')
from agent import MusicAgent 

#全局设置
global all_messages
all_messages = []
global OPENAI_KEY 
OPENAI_KEY = ""
global agent 


#设置环境变量
os.environ["OPENAI_BASE_URL"] = "https://one.aiskt.com/v1/chat" # 注意换成你自己的地址
os.environ["OPENAI_API_KEY"] = "sk-KIRPMVASy9iN8i7GAd67A88f0f8745EdB8D363Eb82305c8b"
# """使用gradio部署Music Agent的demo页面"""
# args = parse_args()
# #agent = MusicAgent(args.config, mode="gradio")
agent = MusicAgent(config_path="config.yaml",mode="gradio")
agent._init_backend_from_env()