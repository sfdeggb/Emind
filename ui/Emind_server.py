import gradio as gr 
from gradio import themes 
from Emind_index_ui import create_emind_index_ui 
from Emind_main_ui import creat_emind_main_ui,create_chat_event_handler
from Emind_paramters_ui import creat_emind_paramter_ui,create_paramters_envent_hander	
from Emind_login import create_emind_login,create_login_event_handler
import os 
from shard import get_css 

# def emind_server():
them = themes.Base.load(os.getcwd()+"/ui/themes/themes_theme_schema@0.0.1_light.json") 
#设置主题为HaleyCH/HaleyCH_Theme
with gr.Blocks(theme=them,title="EMIND -- YOUR MUSIC FRIEND",css=get_css()) as demo:
	#TODO:调用index 界面的gradio ui
	create_emind_index_ui()
	#TODO:调用login 界面的gradio ui
	create_emind_login()
	#TODO:调用chat 界面的gradio ui
	creat_emind_main_ui()
	create_chat_event_handler()
	#TODO:调用paramter 界面的回调函数
	create_login_event_handler()
	#TOSO:调用paramter 界面的gradio ui
	creat_emind_paramter_ui()
	create_paramters_envent_hander()

#启动服务
demo.queue().launch(server_name='0.0.0.0', server_port=8022)

# if __name__ =="__main__":
# emind_server()
