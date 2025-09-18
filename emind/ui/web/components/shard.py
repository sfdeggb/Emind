import os 
import copy 
from pathlib import Path 


#定义所有的项目的gradio 组件
gradio ={}

#定义组件的可见性
chatbot_tab_visible = False
custom_tab_visible = False

#定义自定义组件的参数
settings = {
	"lyrics_path":"['明月几时有 把酒问青天 不知天上宫阙 今夕是何年']",
	"chord_path":"['zh C: G: A:m E: D:m G:']",
	"db_path":"'database/ROC.db'",
	"debug":"False",
	"sentiment":"False",
	"batch_size":"8192",
	"tokenizer":"None",

	"sample_rating":"",
	"offset":"",
	"moon":"",#到这里第一个模型配置参数完了
	#声音识别的参数
	"text_audio_model":"None",
	"pipeline_task":"None",
	"pipeline_tokenizer":"None",
	"pipeline_config":"None",
	#联网搜索的参数
	"spotify_base_url":"None",
	"spotify_key":"None",
	"search_options":"None",
	"google_base_url":"None",
	"google_key":"None",
	"google_eninger":"None",
	#人声分离的参数
	"source_sperate_model":"None",
	"save_file_type":"None",
	"n_job":"None",
	"clip_start_time":"None",
	"clip_end_time":"None",
	#音乐推荐的参数
	"music_recomend_genres":"None",
	"music_recommend_model_with_chinese":"None",
	"music_recommend_model_with_english":"None",
	"music_recommend_model_with_english_based_content":"None",
	
}


default_settings =  copy.deepcopy(settings)

def split_conf(settings):
	"""
	将全局参数拆分为每个模型的参数
	"""

	keys = list(settings.keys())
	#muzic/roc 
	muzic_roc= {key: settings[key] for key in keys[:7]}
	#uknow_model
	unkow_model= {key: settings[key] for key in keys[7:10]}
	#Text2AudioDima or Text2AudioLewtun
	text_audio_model= {key: settings[key] for key in keys[10:14]}
	#spotify
	spotify = {key: settings[key] for key in keys[14:17]}
	#google
	google= {key: settings[key] for key in keys[17:20]}
	#basic_patch
	basic_patch = {key: settings[key] for key in keys[20:23]}
	#basic_crop
	basic_crop= {key: settings[key] for key in keys[23:25]}
	#music_recomandation_spotify
	music_recomandation_spotify= {key: settings[key] for key in keys[25:26]}
	#music_recommend_model
	is_music_recommend_model_with_chinese= {key: settings[key] for key in keys[26:27]}
	is_music_recommend_model_with_english= {key: settings[key] for key in keys[27:28]}
	is_music_recommend_model_with_english_based_content= {key: settings[key] for key in keys[28:29]}

#定义是否成功登录变量
is_login = False

#定义加载插件的变量
load_custom_plugins=False 

#########################################
## DEMO global setting
#########################################
from gradio import themes 

# 修复主题路径
project_root = Path(__file__).parent.parent.parent.parent.parent
theme_path = project_root / "reFdemo" / "themes" / "themes_theme_schema@0.0.1_light.json"

try:
    demo_them = themes.Base.load(str(theme_path))
except:
    # 如果主题文件不存在，使用默认主题
    demo_them = themes.Soft()

demo_css = """
/*调整麦克风的大小*/
#audio {
	height:80px !important;
}
/**调整登录页面的字体大小*/

.gradio-container-4-19-1 .prose h1{
	margin-top: 20px;
}
/**调整三个按钮的大小*/
#send_button,#clear_button,#upload_button{
	height: 80px;
}
"""
demo_title = "EMIND -- YOUR MUSIC FRIEND"
