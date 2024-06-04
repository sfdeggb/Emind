import gradio as gr
from page.shard import gradio
from html_c.gradio_html import html_login


## test function
def login(username, password):
	if username == "admin" and password =="admin":
		welcome ="欢迎回来，{0}".format(username)
		gr.Info(welcome)
		return gr.update(interactive=True)
	else:
		chatbot_tab_visible=False
		raise gr.Error("登录失败,请检查用户名和密码是否正确,刷新页面重试！")
		return gr.update(Interactive=False)


def create_emind_login():
    with gr.Tab("用户登录",elem_id="login_tab") as Login_tab:
        gradio["tab_login"] = Login_tab
        gradio["login_title"] = gr.HTML(html_login())
        gradio["login_user_input_text"] = gr.Textbox(placeholder="请输入用户名", type="text", label="用户名",interactive=True)
        gradio["login_user_pwd_input_text"]  = gr.Textbox(placeholder="请输入密码", type="password", label="密码",interactive=True)
        gradio["login_button"]= gr.Button(value="登录",elem_id="emind_login")
        gradio["login_button"].click(login,[gradio["login_user_input_text"],gradio["login_user_pwd_input_text"]])
        
##
