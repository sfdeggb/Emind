import gradio as gr 
from shard import gradio, chatbot_tab_visible, custom_tab_visible,default_settings,settings
from shard import settings
from untils import create_logging
from Emind_backend import agent, all_messages, OPENAI_KEY

""""
#TODO:在这里的不同地方要加上保存按钮，用于修改参数后,相应的模型能够重载
#模型重载方法agent._update_pipes(name,config)
"""

#创建日志
logger = create_logging("logger_paramter","log_paramter.log")

#创建保存按钮
save_icon= "💾"
#-------------------music_roc model configuration start-------------------
def upload_song_content(file):
    filepath = file.name 
    #example:/tmp/gradio/da39a3ee5e6b4b0d3255bfef95601890afd80709/lyrics.txt(file_path_string)
    settings["lyrics_path"]=filepath 
    logger.info("歌词文件已经配置,路径为{}".format(filepath)) 

def upload_song_chord(file):
    filepath = file.name 
    settings["chord_path"]=filepath 
    logger.info("歌词文件已经配置,路径为{}".format(filepath)) 

def upload_song_db(file):
    filepath = file.name 
    settings["db_path"]=filepath 
    logger.info("歌词文件已经配置,路径为{}".format(filepath)) 
    
def select_debug_options(option):
	if option == "开启":
		option_2 = True 
	else:
		option_2 = False
	settings["debug"]=option_2 
	#for example:开启关闭(string)
	logger.info("调试选项已经配置,选项为{}".format(option))

def select_emotion_options(option):
	if option == "开启":
		option_2 = True
	else:
		option_2 = False
	settings["sentiment"]=option_2 
	logger.info("情绪选项已经配置,选项为{}".format(option))
 
def get_batch_size(batch_size):
    #for example:8192(float)
	settings["batch_size"]=batch_size 
	logger.info("batch size已经配置,选项为{}".format(batch_size))
def select_tokenizer(tokenizer):
    #for example space(string)
	settings["tokenizer"]=tokenizer 
	logger.info("tokenizer已经配置,选项为{}".format(tokenizer))
def get_sample_rating(sample_rating):
	settings["sample_rating"]=sample_rating 
	logger.info("sample rating已经配置,选项为{}".format(sample_rating))
def get_offset(offset):
	settings["offset"]=offset 
	logger.info("offset已经配置,选项为{}".format(offset))
#-------------------music_roc model configuration end-------------------
def select_moon(moon):
	settings["moon"]=moon 
	logger.info("moon已经配置,选项为{}".format(moon))
#---------------------------------speech_rec model configuration start-------------------
def select_text_audio_model(model):
	settings["text_audio_model"]=model 
	logger.info("text_audio_model已经配置,选项为{}".format(model))
def get_pipeline_task(task):
	settings["pipeline_task"]=task 
	logger.info("pipeline_task已经配置,选项为{}".format(task))
def upload_pipeline_tikenizer(file):
	filepath = file.name 
	settings["pipeline_tikenizer"]=filepath 
	logger.info("pipeline_tikenizer已经配置,路径为{}".format(filepath))
def upload_pipeline_config(file):
	filepath = file.name 
	settings["pipeline_config"]=filepath 
	logger.info("pipeline_config已经配置,路径为{}".format(filepath))
def get_spotify_base_url(url):
	settings["spotify_base_url"]=url 
	logger.info("spotify_base_url已经配置,选项为{}".format(url))
def get_spotify_key(key):
	settings["spotify_key"]=key 
	logger.info("spotify_key已经配置,选项为{}".format(key))
def select_search_options(option):
	settings["search_options"]=option 
	logger.info("search_options已经配置,选项为{}".format(option))
def get_google_base_url(url):
	settings["google_base_url"]=url 
	logger.info("google_base_url已经配置,选项为{}".format(url))
def get_google_key(key):	
	settings["google_key"]=key 
	logger.info("google_key已经配置,选项为{}".format(key))
def get_google_eninger(eninger):
	settings["google_eninger"]=eninger 
	logger.info("google_eninger已经配置,选项为{}".format(eninger))
def select_source_sperate_model(model):	
	settings["source_sperate_model"]=model 
	logger.info("source_sperate_model已经配置,选项为{}".format(model))
def select_save_file_type(filetype):
	settings["save_file_type"]=filetype 
	logger.info("save_file_type已经配置,选项为{}".format(filetype))
def get_n_job(n_job):
	settings["n_job"]=n_job 
	logger.info("n_job已经配置,选项为{}".format(n_job))
def get_clip_start_time(clip_start_time):
	settings["clip_start_time"]=clip_start_time 
	logger.info("clip_start_time已经配置,选项为{}".format(clip_start_time))
def get_clip_end_time(clip_end_time):	
	settings["clip_end_time"]=clip_end_time 
	logger.info("clip_end_time已经配置,选项为{}".format(clip_end_time))
def get_music_recomend_genres(genres):
	settings["music_recomend_genres"]=genres 
	logger.info("music_recomend_genres已经配置,选项为{}".format(genres))
def select_music_recommend_model_with_chinese(chinese):
	settings["music_recommend_model_with_chinese"]=chinese 
	logger.info("music_recommend_model_with_chinese已经配置,选项为{}".format(chinese))
def select_music_recommend_model_with_english(english):
	settings["music_recommend_model_with_english"]=english 
	logger.info("music_recommend_model_with_english已经配置,选项为{}".format(english))
def select_music_recommend_model_with_english_based_content(content):
	settings["music_recommend_model_with_english_based_content"]=content 
	logger.info("music_recommend_model_with_english_based_content已经配置,选项为{}".format(content))
 
def save_model_music_gen():
	"""TAB 保存音乐生成模型参数"""
	keys_default = list(default_settings.keys())
	keys= list(settings.keys())
	music_roc_deafult_conf = {key: default_settings[key] for key in keys_default[:7]}
	music_roc_conf = {key: settings[key] for key in keys[:7]}
	#判断是否有改变
	if music_roc_deafult_conf != music_roc_conf:
		try:
			agent._update_pipes("muzic/roc",music_roc_conf)#更新模型:更改参数
			logger.info("音乐生成模型参数已经更新")
			gr.Info("配置成功！")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:
		logger.info("音乐生成模型参数没有改变,无需重载！")

def save_model_speech_rec():
	keys_default = list(default_settings.keys())
	keys= list(settings.keys())
	text_audio_model_default_conf = {key: default_settings[key] for key in keys_default[10:14]}
	text_audio_model_conf = {key: settings[key] for key in keys[10:14]}
	#判断是否有改变
	if text_audio_model_default_conf != text_audio_model_conf:
		try:
			#settings["text_audio_model"] = "dima806/music_genres_classification"
			agent._update_pipes(settings["text_audio_model"],text_audio_model_conf)#更新模型:更改参数
			logger.info("声音识别模型参数已经更新")
			gr.Info("配置成功！")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:
		logger.info("声音识别模型参数没有改变，无需重载！")
  
def save_model_search():
	keys_default = list(default_settings.keys())
	keys= list(settings.keys())
	spotify_default_conf = {key: default_settings[key] for key in keys_default[14:17]}
	spotify_conf = {key: settings[key] for key in keys[14:17]}
	google_default_conf = {key: default_settings[key] for key in keys_default[17:20]}
	google_conf = {key: settings[key] for key in keys[17:20]}
	#判断是否有改变
	if spotify_default_conf != spotify_conf:
		try:
			agent._update_pipes("music_recommand_spotify",spotify_conf)#更新模型:更改参数
			logger.info("spotify模型参数已经更新")
			gr.Info("配置成功！")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:
		logger.info("spotify模型参数没有改变")
	if google_default_conf != google_conf:
		try:
			agent._update_pipes("google-search",google_conf)#更新模型:更改参数
			logger.info("google模型参数已经更新")
			gr.Info("配置成功！")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:
		logger.info("google模型参数没有改变")
  
def save_model_split():
	keys_default = list(default_settings.keys())
	keys= list(settings.keys())
	source_sperate_model_default_conf1 = {key: default_settings[key] for key in keys_default[20:23]}
	source_sperate_model_conf1 = {key: settings[key] for key in keys[20:23]}
	#-----------------
	source_sperate_model_default_conf2 = {key: default_settings[key] for key in keys_default[23:25]}
	source_sperate_model_conf2 = {key: settings[key] for key in keys[23:25]}
	#判断是否有改变
	if source_sperate_model_default_conf1 != source_sperate_model_conf1:
		try:
			agent._update_pipes("basic-pitch",source_sperate_model_conf1)#更新模型:更改参数
			logger.info("人声分离模型参数已经更新")
			gr.Info("配置成功！")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:
		logger.info("人声分离模型参数没有改变,无需重载！")
	if source_sperate_model_default_conf2 != source_sperate_model_conf2:
		try:
			agent._update_pipes("basic-crop",source_sperate_model_conf2)
			logger.info("音频剪辑模型参数已经更新")
		except Exception as e:
			raise gr.Error("重新加载失败！请检查参数配置是否正确！")
	else:	
		logger.info("音频剪辑模型参数没有改变")

def save_model_music_rec():
	keys_default = list(default_settings.keys())
	keys= list(settings.keys())
	music_recomandation_spotify_default_conf = {key: default_settings[key] for key in keys_default[25:26]}
	music_recomandation_spotify_conf = {key: settings[key] for key in keys[25:26]}
	#-----------------
	is_music_recommend_model_with_chinese_default_conf = {key: default_settings[key] for key in keys_default[26:27]}
	is_music_recommend_model_with_chinese_conf = {key: settings[key] for key in keys[26:27]}
	#-----------------
	is_music_recommend_model_with_english_default_conf = {key: default_settings[key] for key in keys_default[27:28]}
	is_music_recommend_model_with_english_conf = {key: settings[key] for key in keys[27:28]}
	#-----------------
	is_music_recommend_model_with_english_based_content_default_conf = {key: default_settings[key] for key in keys_default[28:29]}
	is_music_recommend_model_with_english_based_content_conf = {key: settings[key] for key in keys[28:29]}
	#判断是否有改变
	try:
		if music_recomandation_spotify_default_conf != music_recomandation_spotify_conf:
			agent._update_pipes("music_recommand_spotify",music_recomandation_spotify_conf)#更新模型:更改参数
			logger.info("音乐推荐模型参数已经更新")
		else:
			logger.info("音乐推荐模型参数没有改变")
		if is_music_recommend_model_with_chinese_default_conf != is_music_recommend_model_with_chinese_conf:
			agent._delete_pipes("music_recommand_Chinese",is_music_recommend_model_with_chinese_conf)#更新模型:更改参数
			logger.info("中文音乐推荐模型参数已经更新")
		else:
			logger.info("中文音乐推荐模型参数没有改变")
		if is_music_recommend_model_with_english_default_conf != is_music_recommend_model_with_english_conf:
			agent._delete_pipes("music_recommand_english",is_music_recommend_model_with_english_conf)#更新模型:更改参数
			logger.info("英文音乐推荐模型参数已经更新")
		if is_music_recommend_model_with_english_based_content_default_conf != is_music_recommend_model_with_english_based_content_conf:
			agent._delete_pipes("music_recommand_content",is_music_recommend_model_with_english_based_content_conf)	
			logger.info("基于内容的英文音乐推荐模型参数已经更新")
		else:
			logger.info("基于内容的英文音乐推荐模型参数没有改变")
		gr.Info("配置成功！")
	except Exception as e:
		raise gr.Error("重新加载失败！请检查参数配置是否正确！")

def creat_emind_paramter_ui():
	with gr.Tab("自定义配置",elem_id="custom_config",visible=False) as Argument_tab:
		gradio["Argument_tab"] = Argument_tab
		#muzic roc 模型的参数配置页
		with gr.Tab(label="音乐生成",elem_id="music_roc") as Music_roc_tab:
			gradio["Music_roc_tab"] = Music_roc_tab
			with gr.Row(elem_id="model_paramters"):
				"""在gradio3.37.0中type 没有filepath,只有file,所以这里的type="filepath"需要修改为type="file，取得文件名用file.name"""
				gradio["song_content"] = gr.File(label="歌词文件(.txt)",type="file",interactive=True)#歌词路径
				gradio["song_chord"] = gr.File(label="和弦文件.txt", type="file",interactive=True)#弦乐文件
				gradio["song_db"] = gr.File(label="音乐数据库", type="file",interactive=True)#数据库文件
				gradio["debug"]=  gr.Radio(choices=["开启","关闭"],label="调试选项",value="store_true",interactive=True)#调试选项
				gradio["sentiment"]=  gr.Radio(choices=["开启","关闭"],label="情绪基调",value="store_true",interactive=True)
			with gr.Row(elem_id="load_paramters",equal_height=False):
				with gr.Column(elem_id="roc_paramters"):
					gradio["batch_size"] =  gr.Slider(minimum=0, maximum=10000, step= 1,value=8192,label="训练速度",min_width=500)#batch size
					gradio["tokenizer"]=  gr.Radio(choices=["space","subword_nmt", "sentencepiece"],label="切割机",
						value="space",interactive=True) #tokiner 名称
				with gr.Column(elem_id="other_models_paramters"):
					gradio["sample_rating"] = gr.Slider(minimum=10000, maximum=22050, step= 1,value=16000,label="采样率")#sampling rate
					gradio["offset"] = gr.Slider(minimum=0, maximum=10000, step= 1,value=0,label="偏移",elem_id="music_gen_offset")#offset
			with gr.Row(elem_id="save_model",equal_height=False):
				gradio["music_gen_save_button"]= gr.Button(save_icon,onclick=save_model_music_gen(),elem_id="save_model_gen",label="保存",placeholder="保存配置")
    
		with gr.Tab(label="声音识别"):
			gradio["text_audio_model"]  = gr.Radio(
       		choices=["dima806/music_genres_classification","lewtun/distilhubert-finetuned-music-genres"],
            type="value",label="模型选择")
			gradio["pipeline_task"] = gr.Textbox(value="audio-classification", type="text" ,lines=1,label="任务类型",interactive=True)#任务类型
			with gr.Row():
				gradio["pipeline_tikenizer"] = gr.File(label="切割机", type="file",interactive=True)#分词器
				gradio ["pipeline_config"]= gr.File(label="配置文件", type="file",interactive=True)#配置文件
				gradio["framework"]=gr.Radio(choices=["TF","PT"],label="框架",value="tf",interactive=True)#调试选项
			with gr.Row():
				gradio["speech_rec_save_button"]= gr.Button(save_icon,onclick=save_model_speech_rec,elem_id="save_model_speech",label="保存",placeholder="保存配置")
		
		with gr.Tab(label="联网搜索"):#spotify,google search
			with gr.Row():#spotify
				gradio["spotify_base_url"]= gr.Textbox(value="https://api.spotify.com/v1/", type="text" ,lines=1,label="音乐基础地址",interactive=True)
				gradio["spotify_key"]=gr.Textbox(value="xxxxxxxxxxxxx", type="password" ,lines=1,label="密钥",interactive=True)
				gradio["search_options"]= gr.Radio(choices=["search","track","album","artist","genre","description"],label="搜索目标",value="search",interactive=True)
			with gr.Row():#google search
				gradio["google_base_url"]=gr.Textbox(value="https://www.googleapis.com/customsearch/v1", type="text" ,lines=1,label="Google基础地址",interactive=True)
				gradio["google_key"]= gr.Textbox(value="xxxxxxxxxxxxx", type="password" ,lines=1,label="密钥",interactive=True)
				gradio["google_eninger"] =gr.Textbox(value="xxxxxxxxxxxxx", type="text" ,lines=1,label="搜索引擎(id)",interactive=True)
			with gr.Row():
				gradio["internet_save_model"]= gr.Button(save_icon,onclick=save_model_search,elem_id="save_model_search",label="保存",placeholder="保存配置")
    
		with gr.Tab(label="人声分离"):
			with gr.Row():#model
				gradio["source_sperate_model"]=gr.Radio(choices=["htdemucs","htdemucs_ft","hdemucs_mmi","mdx"],value="htdemucs",label="模型选择",interactive=True)
			with gr.Row():#specillay
				gradio["save_file_type"] = gr.Radio(choices=["wav","mp3"],label="文件格式",value="wav",interactive=True)
				gradio["n_job"] = gr.Slider(minimum=0, maximum=5, step= 1,value=2,label="分离速度",interactive=True)#parrallel
			with gr.Row():#basic_opertate
				gradio["clip_start_time"] = gr.Slider(minimum=-1, maximum=360, step= 1,value=0,label="开始剪辑时间",interactive=True)
				gradio["clip_end_time"]= gr.Slider(minimum=-1, maximum=360, step= 1,value=0,label="终止剪辑时间",interactive=True)
			with gr.Row():
				gradio["split_save_model"] = gr.Button(save_icon,onclick=save_model_split,elem_id="save_model_split",label="保存",placeholder="保存配置")

  		# with gr.Tab(label="music_genreate"):
		# 	gr.Slider(minimum=10000, maximum=22050, step= 1,value=16000,label="sampling rate")
		# 	gr.Radio(choices=["True","False"],label="moon",value="wav",interactive=True)
		# 	gr.Slider(minimum=0, maximum=10000, step= 1,value=0,label="offset")
		with gr.Tab(label="音乐推荐"):#TODO:
			gradio["music_recomend_genres"]=gr.Dropdown(choices=["pop","world_music","folk","forro"],value="pop",label="音乐类型",interactive=True)
			gradio["music_recommend_model_with_chinese"]=gr.Radio(choices=["True","False"],label="中文模型",value="True",interactive=True)
			gradio["music_recommend_model_with_english"]=gr.Radio(choices=["True","False"],label="英文模型",value="True",interactive=True)
			gradio["music_recommend_model_with_english_based_content"]=gr.Radio(choices=["True","False"],label="基于内容的英文模型",value="True",interactive=True)
			with gr.Row():
				gradio["music_recommend_save_model"]= gr.Button(save_icon,onclick=save_model_music_rec,elem_id="save_model_rec",label="保存",placeholder="保存配置")
#事件监听，调用处理函数

def create_paramters_envent_hander():
    #音乐生成事件回调
	gradio["song_content"].upload(upload_song_content,[gradio["song_content"]])
	gradio["song_chord"].upload(upload_song_chord,[gradio["song_chord"]])
	gradio["song_db"].upload(upload_song_db,[gradio["song_db"]])
	gradio["debug"].change(select_debug_options,[gradio["debug"]])
	gradio["sentiment"].change(select_emotion_options,[gradio["sentiment"]])
	gradio["batch_size"].change(get_batch_size,[gradio["batch_size"]])
	gradio["tokenizer"].change(select_tokenizer,[gradio["tokenizer"]])
	gradio["music_gen_save_button"].click(save_model_music_gen)
	#下面是另一个音乐模型
	gradio["sample_rating"].change(get_sample_rating,[gradio["sample_rating"]])
	gradio["offset"].change(get_offset,[gradio["offset"]])
	#gradio["moon"].select(select_moon,[gradio["moon"]])
	#声音识别
	gradio["text_audio_model"].change(select_text_audio_model,[gradio["text_audio_model"]])
	gradio["pipeline_task"].change(get_pipeline_task,[gradio["pipeline_task"]])
	gradio["pipeline_tikenizer"].upload(upload_pipeline_tikenizer,[gradio["pipeline_tikenizer"]])
	gradio["pipeline_config"].upload(upload_pipeline_config,[gradio["pipeline_config"]])
	gradio["speech_rec_save_button"].click(save_model_speech_rec)
	#联网搜索
	gradio["spotify_base_url"].blur(get_spotify_base_url,[gradio["spotify_base_url"]])
	gradio["spotify_key"].blur(get_spotify_key,[gradio["spotify_key"]])
	gradio["search_options"].change(select_search_options,[gradio["search_options"]])
	gradio["google_base_url"].blur(get_google_base_url,[gradio["google_base_url"]])
	gradio["google_key"].blur(get_google_key,[gradio["google_key"]])
	gradio["google_eninger"].blur(get_google_eninger,[gradio["google_eninger"]])
	gradio["internet_save_model"].click(save_model_search)
	#人声分离
	gradio["source_sperate_model"].change(select_source_sperate_model,[gradio["source_sperate_model"]])
	gradio["save_file_type"].change(select_save_file_type,[gradio["save_file_type"]])
	gradio["n_job"].change(get_n_job,[gradio["n_job"]])
	gradio["clip_start_time"].change(get_clip_start_time,[gradio["clip_start_time"]])
	gradio["clip_end_time"].change(get_clip_end_time,[gradio["clip_end_time"]])
	gradio["split_save_model"].click(save_model_split)
	#音乐推荐
	gradio["music_recomend_genres"].input(get_music_recomend_genres,[gradio["music_recomend_genres"]])
	gradio["music_recommend_model_with_chinese"].change(select_music_recommend_model_with_chinese,[gradio["music_recommend_model_with_chinese"]])
	gradio["music_recommend_model_with_english"].change(select_music_recommend_model_with_english,[gradio["music_recommend_model_with_english"]])
	gradio["music_recommend_model_with_english_based_content"].select(select_music_recommend_model_with_english_based_content,[gradio["music_recommend_model_with_english_based_content"]])
	gradio["music_recommend_save_model"].click(save_model_music_rec)

css="""
# music_gen_offset{
	height:75px;
}
# other_models_paramters{
	height:150px;
}

"""
if __name__ == "__main__":
	with gr.Blocks() as demo:
		creat_emind_paramter_ui()
		create_paramters_envent_hander()
	demo.launch(server_port=8022)
	

