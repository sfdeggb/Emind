import gradio as gr
from shard import gradio, chatbot_tab_visible, custom_tab_visible,is_login
from html_c.gradio_html import html_login
from html_c.gradio_html import html_register
import pymysql 
import secrets
import datetime 
from datetime import datetime

def create_db_connection():
    #连接数据库
	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="123456",
		database="music_rec",
		cursorclass=pymysql.cursors.DictCursor
	)
	return connection

def login_db(username, password):
	#TODO:最好是链接到数据库做查询验证
	connection = create_db_connection()
	login_statement = "SELECT * FROM music_user WHERE user_name = '{0}' AND password = '{1}'".format(username, password)
	try:
		with connection.cursor() as cursor:
			cursor.execute(login_statement)
			result = cursor.fetchone()
			if result["count"]>0:
				welcome ="欢迎回来，{0}".format(username)
				gr.Info(welcome)
				return gr.update(interactive=True)
			else:
				raise gr.Error("登录失败,请检查用户名和密码是否正确,刷新页面重试！")
	except Exception as e:
		raise gr.Error("登录失败,请检查用户名和密码是否正确,刷新页面重试！")

def login(username, password):
	if username == "admin" and password =="admin":
		welcome ="欢迎回来，{0}".format(username)
		gr.Info(welcome)
		return gr.update(interactive=True)
	else:
		chatbot_tab_visible=False
		raise gr.Error("登录失败,请检查用户名和密码是否正确,刷新页面重试！")
		return gr.update(Interactive=False)

def get_current_date():
    # 获取当前日期
    today = datetime.today()
    # 格式化日期为 YYYY-MM-DD
    formatted_date = today.strftime('%Y-%m-%d')
    # 去掉月份和日期的前导零
    formatted_date = formatted_date.replace('-0', '-')
    return formatted_date

def register_user(username, password, email):
	if username and password and email:
		connection = create_db_connection()
		register_statement = "INSERT INTO music_user (user_id,user_name, password, login_time,register_time) VALUES ('{0}', '{1}', '{2}', '{3}','{4}')".format(secrets.token_hex(40 // 2),username, password, get_current_date(),get_current_date())
		try:
			with connection.cursor() as cursor:
				cursor.execute(register_statement)
				connection.commit()
				gr.Info(f"用户 {username} 注册成功！") 
		except Exception as e:
			raise gr.Error("注册失败,请检查用户名和密码是否正确,刷新页面重试！")
	else:
		raise gr.Error("请填写所有字段。")

def create_emind_login():
	with gr.Tab("用户登录",elem_id="login_tab") as Login_tab:
		#登录界面
		gradio["login_title"] = gr.HTML(html_login())
		gradio["user_input_text"] = gr.Textbox(placeholder="请输入用户名", type="text", label="用户名",interactive=True)
		gradio["user_pwd_input_text"]  = gr.Textbox(placeholder="请输入密码", type="password", label="密码",interactive=True)
		gradio["login_button"]= gr.Button(value="登录",elem_id="emind_login")
		#gradio["txt"] = gr.Textbox(placeholder="登录提示", type="text", label="提示",interactive=False)
		gradio["register_link"] = gr.Button("没有账号先注册")
		#设置事件监听
	with gr.Tab("用户注册",elem_id="register_tab") as Register_tab:
		#注册界面
		gradio["register_title"] = gr.HTML(html_register())
		gradio["user_register_input_text"] = gr.Textbox(placeholder="请输入用户名", type="text", label="用户名",interactive=True)
		gradio["user_register_pwd_input_text"]  = gr.Textbox(placeholder="请输入密码", type="password", label="密码",interactive=True)
		gradio["register_email"] = gr.Textbox(label="电子邮件")
		gradio["register_button"]= gr.Button(value="注册",elem_id="emind_register")
		#gradio["txt"] = gr.Textbox(placeholder="登录提示", type="text", label="提示",interactive=False)
		#设置事件监听
def create_login_event_handler():
    #输出组件是什么
	gradio["login_button"].click(login,[gradio["user_input_text"],gradio["user_pwd_input_text"]],gradio["txt"])
	gradio["register_button"].click(register_user,
                                 	[gradio["user_register_input_text"],
                                    gradio["user_register_pwd_input_text"],
                                    gradio["register_email"]]
                                 	,gradio["txt"])
if __name__ == "__main__":
	with gr.Blocks() as demo:
		create_emind_login()
		create_login_event_handler()
	demo.queue().launch(server_port=8022)
	#register_user("test","test","zjmac1635@163.com")
