import os 
import re 
import uuid
import requests
import soundfile
import argparse
from transformers import pipeline 
import gradio as gr 
import numpy as np 
from gradio import themes 
from  shard import gradio, chatbot_tab_visible, custom_tab_visible
from html_c.gradio_html import get_head
from Emind_backend import agent, all_messages, OPENAI_KEY
import torch 
from emotion.emo_analyse import QEmo

# agent= 
# all_messages 
# OPENAI_KEY

def add_text_to_symbol(file_path, text_to_insert):
    with open(file_path, 'r',encoding="utf-8") as file:
        lines = file.readlines()

    start_index = None
    end_index = None

    for i, line in enumerate(lines):
        if 'Answer in the language of Chinese.' in line:
            start_index = i
        elif '[CONTEXT]' in line:
            end_index = i
            break
    if start_index is not None and end_index is not None:
        del lines[start_index + 1:end_index]

        lines.insert(start_index + 1, text_to_insert + '\n')

    with open(file_path, 'w') as file:
        file.writelines(lines)

        
def analyze_emotion(messages):
    text=""
    for message in messages:
        if message["role"] == "user":
            text+=message["content"]
    emotion = QEmo()
    result = emotion.emo(text)
    emo=emotion.get_emotion(result)
    #let the assistant know the emotion of the user
    instructions = f"""You can adjust the tone of your responses based on the user's emotions,the user's current mood is {emo}"""
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to skprompt.txt
    skprompt_path = os.path.join(current_dir, '..', 'skills/MusicAgent','ChatBot', 'skprompt.txt')
    add_text_to_symbol(skprompt_path, instructions)

def add_message(content, role):
    #构成请求的消息列表
    message = {"role": role, "content": content}
    all_messages.append(message)
    analyze_emotion(all_messages)

def extract_medias(message):
    # audio_pattern = re.compile(r"(http(s?):|\/)?([\.\/_\w:-])*?\.(flac|wav|mp3)")
    audio_pattern = re.compile(r"(http(s?):|\/)?[a-zA-Z0-9\/.:-]*\.(flac|wav|mp3)")
    symbolic_button = re.compile(r"(http(s?):|\/)?[a-zA-Z0-9\/.:-]*\.(mid)")

    audio_urls = []
    for match in audio_pattern.finditer(message):
        if match.group(0) not in audio_urls:
            audio_urls.append(match.group(0))

    symbolic_urls = []
    for match in symbolic_button.finditer(message):
        if match.group(0) not in symbolic_urls:
            symbolic_urls.append(match.group(0))

    return list(set(audio_urls)), list(set(symbolic_urls))

def set_openai_key(openai_key):
    """通过输入OpenAI API Key来设置全局变量OPENAI_KEY"""
    global OPENAI_KEY
    OPENAI_KEY = openai_key
    agent._init_backend_from_input(openai_key)  
     
    if not OPENAI_KEY.startswith("sk-"):
        return "OpenAI API Key starts with sk-", gr.update(visible=False)

    return OPENAI_KEY, gr.update(visible=True)

def parse_lyric_result(result):
    temp_sentence = ""
    counter = 0  # 计数器
    try:
        finally_task_id = list(result.keys())[-1]
        finally_task = result[finally_task_id]
        inference_result = finally_task["inference result"]
        for inf in inference_result:
            if "lyric" in inf.keys():
                for lyric in inf["lyric"]:
                    if counter % 2 == 1:  # 每两句之间加逗号
                        temp_sentence += ","+lyric
                    else:
                        temp_sentence += lyric
                    counter += 1
                    if counter % 2 == 0:  # 每两句之后加换行符
                        temp_sentence += "\n"
    except Exception as e:
        print(e)
        temp_sentence = ""
    return temp_sentence
        
def add_text(messages, message):
    add_message(message, "user")
    messages = messages + [(message, None)]
    audio_urls, _ = extract_medias(message)

    for audio_url in audio_urls:
        if audio_url.startswith("http"):
            ext = audio_url.split(".")[-1]
            name = f"{str(uuid.uuid4()[:4])}.{ext}"
            response = requests.get(audio_url)
            with open(f"{agent.config['src_fold']}/{name}", "wb") as f:
                f.write(response.content)
            messages = messages + [(None, f"{audio_url} is saved as {name}")]

    return messages, ""

def upload_audio(file, messages):
    file_name = str(uuid.uuid4())[:4]
    audio_load, sr = soundfile.read(file.name)
    soundfile.write(f"{agent.config['src_fold']}/{file_name}.wav", audio_load, samplerate=sr)

    messages = messages + [(None, f"Audio is stored in wav format as ** {file_name}.wav **"), 
                           (None, (f"{agent.config['src_fold']}/{file_name}.wav",))]
    return messages

def bot(messages):
    message, results = agent.chat(messages[-1][0])

    lyric = parse_lyric_result(results)
    #messages = messages + [(None, f"**歌词**\n{lyric}")]
    message = message +"\n"+lyric
    #audio_urls, symbolic_urls = extract_medias(message)
    audio_urls, symbolic_urls = extract_medias(str(results))
    add_message(message, "assistant")
    messages[-1][1] = message
    for audio_url in audio_urls:
        if not audio_url.startswith("http") and not audio_url.startswith(agent.config['src_fold']):
            audio_url =  os.path.join(agent.config['src_fold'], audio_url)
        messages = messages + [(None, f"** {audio_url.split('/')[-1]} **"),
                                (None, (audio_url,))]
    
    for symbolic_url in symbolic_urls:
        if not symbolic_url.startswith(agent.config['src_fold']):
            symbolic_url = os.path.join(agent.config['src_fold'], symbolic_url)
        
        try:
            os.system(f"midi2ly {symbolic_url} -o {symbolic_url}.ly; lilypond -f png -o {symbolic_url} {symbolic_url}.ly")
        except:
            continue
        messages = messages + [(None, f"** {symbolic_url.split('/')[-1]} **")]
        
        if os.path.exists(f"{symbolic_url}.png"):
            messages = messages + [ (None, (f"{symbolic_url}.png",))]
        else:
            s_page = 1
            while os.path.exists(f"{symbolic_url}-page{s_page}.png"):
                messages = messages + [ (None, (f"{symbolic_url}-page{s_page}.png",))]
                s_page += 1
        
    def truncate_strings(obj, max_length=128):
        if isinstance(obj, str):
            if len(obj) > max_length:
                return obj[:max_length] + "..."
            else:
                return obj
        elif isinstance(obj, dict):
            return {key: truncate_strings(value, max_length) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [truncate_strings(item, max_length) for item in obj]
        else:
            return obj

    results = truncate_strings(results)
    results = sorted(results.items(), key=lambda x: int(x[0]))
    response = [(None, "\n\n".join([f"Subtask {r[0]}:\n{r[1]}" for r in results]))]

    #return messages, response
    return messages

def clear_all_history(messages):
    agent.clear_history()

    messages = messages + [((None, "All LLM history cleared"))]
    return messages

def parse_args():
    parser = argparse.ArgumentParser(description="music agent config")
    parser.add_argument("-c", "--config", type=str, help="a YAML file path.")

    args = parser.parse_args()
    return args

def audio_to_text(audio):
	sr, y = audio#sr是采样率，y是16位整形音频数据
	y = y.astype(np.float32)
	y /= np.max(np.abs(y))
	#load the model
	device = torch.device('cuda:0')
	model = pipeline("automatic-speech-recognition", 
					model="/root/muzic/musicagent/models/jonatasgrosman/whisper-large-zh-cv11", device="cuda:0")
	#model.model.to("cpu")
	model.model.to(device)
	model.model.cuda()
	model.model.config.forced_decoder_ids = (
	model.tokenizer.get_decoder_prompt_ids(
		language="zh", 
		task="transcribe"
	)
	)
	speech_text = model({"sampling_rate": sr, "raw": y})["text"]
	return speech_text

#---------------
#发送图标🏃‍♂️
#情况图标🔄
#上传图标☁️
#---------------
def creat_emind_main_ui():
    #主交互界面页
    with gr.Tab("聊天交互",elem_id="main_chat",visible=False) as Chatbot_tab:
        #添加主TAB 组件
        gradio["Chatbot_tab"] = Chatbot_tab
        with gr.Row(visible=True) as Interact_window:
            gradio["Interact_window"] = Interact_window
            #.style(height=500)
            gradio["chatbot"] = gr.Chatbot([],elem_id="chatbot",label="EMIND 助手",height=250)
        with gr.Row() as Chatbot_input:
            #scale=1
            gradio["Chatbot_input"] = Chatbot_input
            with gr.Row():
                with gr.Column(scale=0.6):
                    gradio["txt"] = gr.Textbox(show_label=False, lines = 2,max_lines=10,
                                     placeholder="你可以干什么？按下发送或者回车", elem_id="txt",interactive=False)
                with gr.Column(scale=0.1):
                    gradio["Microphone"]=gr.Microphone(label="🔊点击讲话", elem_id="audio",
                                  min_width=500)
                with gr.Column(scale=0.1, min_width=0):
                    gradio["run"] = gr.Button("发送",size="lg",elem_id="send_button")
                with gr.Column(scale=0.1, min_width=0):
                    gradio["clear_txt"] = gr.Button("清空",size="lg",elem_id="clear_button")
                with gr.Column(scale=0.1, min_width=0):
                    gradio["btn"] = gr.UploadButton("音乐", size = "lg",file_types=["audio"],elem_id="upload_button")
        gradio["examples"] = gr.Examples(
            examples=["你可以做什么?",
                      "生成一首古风中文歌",
                      "推荐几首中文流行歌曲",
                      "推荐几首英文流行歌曲",
                        "写一段最近关于小米SU7的歌词",
                        "下载一首张靓颖的歌曲并把人声和伴奏分离",
                        "将音频转换成小提琴的声音。",
                        "近一个月流行的音乐类型",
                        "将视频中的人声搭配合适的旋律变成一首歌"
            ],
            inputs=gradio["txt"]
    )

def create_chat_event_handler():
    #事件监听，调用处理函数
    gradio["clear_txt"].click(clear_all_history, [gradio["chatbot"]], [gradio["chatbot"]])
    gradio["btn"].upload(upload_audio, [gradio["btn"], gradio["chatbot"]], [gradio["chatbot"]])        
    #运行
    gradio["run"].click(add_text, [gradio["chatbot"], gradio["txt"]], [gradio["chatbot"], gradio["txt"]]).then(
    bot, gradio["chatbot"], [gradio["chatbot"]]
    )
    #提交
    gradio["txt"].submit(add_text, [gradio["chatbot"], gradio["txt"]], [gradio["chatbot"],gradio["txt"]]).then(
    bot, gradio["chatbot"], [gradio["chatbot"]]
    )
    #语音输入--->文本
    gradio["Microphone"].change(audio_to_text, [gradio["Microphone"]], [gradio["txt"]])
if __name__ == "__main__":
    with gr.Blocks(css=get_css()) as demo:
        #创建主交互界面
        creat_emind_main_ui()
        #创建事件监听
        #create_chat_event_handler()
        #启动主交互界面
    demo.launch()