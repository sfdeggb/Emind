import gradio as gr 
from html_c.gradio_html import get_index_html
from page.shard import gradio

def create_emind_index_ui():
    with gr.Tab("首页",elem_id="index_tab") as Index_tab:
        gradio["tab_index"] = Index_tab
        gradio["index_page"] = gr.HTML(get_index_html())
