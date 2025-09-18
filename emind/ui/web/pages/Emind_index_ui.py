import gradio as gr 
from html_c.gradio_html import get_index_html
from html_c.gradio_html import get_sample_html 
from shard import gradio, chatbot_tab_visible, custom_tab_visible

def create_emind_index_ui():
    with gr.Tab("首页",elem_id="index_tab") as Index_tab:
        gradio["Index_tab"] = Index_tab
        #首页界面
        title = gr.HTML(get_index_html())
        gradio["title"] = title
    #设置事件监听--没有

if __name__=="__main__":
    with gr.Blocks(title="Emind首页")as demo :
        create_emind_index_ui()

    demo.launch()

