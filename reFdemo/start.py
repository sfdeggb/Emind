import gradio as gr 

from page.emind_index import create_emind_index_ui 
from page.emind_chat import creat_emind_main_ui
from page.emind_setting import creat_emind_paramter_ui,create_paramters_envent_hander	
from page.emind_login import create_emind_login
from page.emind_users import create_emind_userinfo

from page.shard import demo_them, demo_css, demo_title

#设置主题为HaleyCH/HaleyCH_Theme
with gr.Blocks(theme=demo_them,title=demo_title,css=demo_css) as demo:
    create_emind_index_ui()
    create_emind_login()
    create_emind_userinfo()
    creat_emind_main_ui()
    creat_emind_paramter_ui()
    create_paramters_envent_hander()
    
 
demo.queue().launch(server_name='0.0.0.0', server_port=8022)
