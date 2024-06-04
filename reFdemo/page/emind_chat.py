import os 
import re 
import uuid
import requests
import soundfile
import argparse
import torch 
from transformers import pipeline 
import gradio as gr 
import numpy as np 

from page.shard import gradio, chatbot_tab_visible, custom_tab_visible
from page.agent_setting import agent, all_messages, OPENAI_KEY


# agent= 
# all_messages 
# OPENAI_KEY

def add_message(content, role):
    #构成请求的消息列表
    message = {"role": role, "content": content}
    all_messages.append(message)

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
    try:
        finally_task_id = list(result.keys())[-1]
        finally_task = result[finally_task_id]
        inference_result = finally_task["inference result"]
        for inf in inference_result:
            if "lyric" in inf.keys():
                for lyric in inf["lyric"]:
                    temp_sentence += lyric+"\n"
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
    with gr.Tab("聊天交互",elem_id="main_chat",visible=False) as Chatbot_tab:
        #添加主TAB 组件
        gradio["tab_chat"] = Chatbot_tab
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
                        "写一段歌词关于最近世界杯的比赛",
                        "下载一首周杰伦的歌曲,并把人声和伴奏分离",
                        "把/b.wav的人声转换成小提琴的声音。",
                        "近一个月流行的音乐类型",
                        "把c.wav中的人声搭配合适的旋律变成一首歌"
            ],
            inputs=gradio["txt"]
        )
        ## handel
        gradio["clear_txt"].click(clear_all_history, [gradio["chatbot"]], [gradio["chatbot"]])
        gradio["btn"].upload(upload_audio, [gradio["btn"], gradio["chatbot"]], [gradio["chatbot"]])        
        # run
        gradio["run"].click(add_text, [gradio["chatbot"], gradio["txt"]], [gradio["chatbot"], gradio["txt"]]).then(
        bot, gradio["chatbot"], [gradio["chatbot"]])
        # submit
        gradio["txt"].submit(add_text, [gradio["chatbot"], gradio["txt"]], [gradio["chatbot"],gradio["txt"]]).then(
        bot, gradio["chatbot"], [gradio["chatbot"]])
        # mic input to txt
        gradio["Microphone"].change(audio_to_text, [gradio["Microphone"]], [gradio["txt"]])