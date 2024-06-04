import gradio as gr
from page.shard import gradio

def create_emind_userinfo():
    with gr.Tab("用户信息",elem_id="tab_userinfo") as tab_userinfo:
        gradio["tab_userinfo"] = tab_userinfo
        gradio["1"] = gr.Label(label="用户名")
        gradio["2"] = gr.Label(label="密码")
        gradio["3"] = gr.Textbox(placeholder="请输入用户名", type="text", label="用户名",interactive=False)
        gradio["4"]  = gr.Textbox(placeholder="请输入密码", type="password", label="密码",interactive=False)
        ## todo
        ## 单独显示信息
        with gr.Row():
            gradio["5"] = gr.Textbox(label="123", type="text",interactive=True)
            gradio["6"]= gr.Textbox(label="123", type="text",interactive=True)