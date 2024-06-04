import os 

def get_head():
    html_content = """
    <div style='text-align: center;'>
    <h1>🎧 EMIND</h1>
    <h2>YOUR CONFIDENT</h2>
    </div>
    """
    return html_content

def get_index_html():
    html_content = """
    <!DOCTYPE html>
    <html lang="en" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#">

    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">
    <!-- The above 3 meta tags must come first in the head; any other head content comes after -->

    <title>Mood light | Screensaver for chillaxing, meditation, sleeping</title>
    <meta name="description" content="Color changing ambient mood lights - nice place to slow down and relax.">
    <meta name="keywords" content="ocean sound, relaxation">
    <meta name="robots" content="index,follow">
    <link rel="canonical" href="https://defonic.com/moodlight.html">

    <!-- For IE 11, Chrome, Firefox, Safari, Opera -->
    <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-96x96.png" sizes="96x96" type="image/png">
    <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-192x192.png" sizes="192x192" type="image/png">
    <link rel="apple-touch-icon" sizes="57x57" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="152x152"
        href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180"
        href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-180x180.png">

    <meta property="og:url" content="https://defonic.com/moodlight.html">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Mood light">
    <meta property="og:description" content="Screensaver for chillaxing, meditation, sleeping.">
    <meta property="og:image" content="https://defonic.com/screensaver/tw.jpg">


    <!-- Google fonts -->
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">

    <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/reset.min.css">
    <link rel="stylesheet"
        href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/font-awesome.min.css">
    <link href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/css" rel="stylesheet">
    <!-- Ensemble style.css + loader.css -->
    <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style.css">
    <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style(1).css">
    <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style(2).css">
  
    </head>

    <body onload="initClock()" data-pagenote="1" data-version="4.0.5" data-settings-changed-at="0" data-cid="1707904580053">

    <svg viewBox="0 0 200 100" preserveAspectRatio="xMidYMid slice" width=100% height=100%>
    <!-- 定以重复使用的元素-->
        <defs>
        <radialgradient id="Gradient1" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="34s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255, 0, 255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255, 0, 255, 0)"></stop>
        </radialgradient>
        <radialgradient id="Gradient2" cx="50%" cy="50%" fx="10%" fy="50%" r=".5">
            <animate attributeName="fx" dur="23.5s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255, 255, 0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255, 255, 0, 0)"></stop>
        </radialgradient>
        <radialgradient id="Gradient3" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="21.5s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0, 255, 255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0, 255, 255, 0)"></stop>
        </radialgradient>

        <radialgradient id="Gradient4" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="23s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0, 255, 0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0, 255, 0, 0)"></stop>
        </radialgradient>
        <radialgradient id="Gradient5" cx="50%" cy="50%" fx="10%" fy="50%" r=".5">
            <animate attributeName="fx" dur="24.5s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0,0,255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0,0,255, 0)"></stop>
        </radialgradient>
        <radialgradient id="Gradient6" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="25.5s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255,0,0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255,0,0, 0)"></stop>
        </radialgradient>
        </defs>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient1)">
        <animate attributeName="x" dur="20s" values="25%;0%;25%" repeatCount="indefinite"></animate>
        <animate attributeName="y" dur="21s" values="0%;25%;0%" repeatCount="indefinite"></animate>
        <animatetransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="100000s"
            repeatCount="indefinite"></animatetransform>
        </rect>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient2)">
        <animate attributeName="x" dur="23s" values="-25%;0%;-25%" repeatCount="indefinite"></animate>
        <animate attributeName="y" dur="24s" values="0%;50%;0%" repeatCount="indefinite"></animate>
        <animatetransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="18s"
            repeatCount="indefinite"></animatetransform>
        </rect>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient3)">
        <animate attributeName="x" dur="25s" values="0%;25%;0%" repeatCount="indefinite"></animate>
        <animate attributeName="y" dur="26s" values="0%;25%;0%" repeatCount="indefinite"></animate>
        <animatetransform attributeName="transform" type="rotate" from="360 50 50" to="0 50 50" dur="19s"
            repeatCount="indefinite"></animatetransform>
        </rect>

        <text x="50" y="50" text-anchor="middle" font-size="20" fill="white">EMIND</text>
        <text x="50" y="60" text-anchor="middle" font-size="6" fill="white" id = "animatedText">新一代AI音乐智能体</text>
        <text x="70" y="70" text-anchor="middle" font-size="4" fill="white" id ="proIntro">---音乐生成和推荐系统</text>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        #animatedText {
        opacity: 0;
        animation: fadeIn 2s forwards;
        animation-delay: 1s; /* 延迟开始动画 */
        }
    </style>
  </svg>

    <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/jquery.min.js.下载"></script>
    <script type="text/javascript"
        src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/share.js.下载"></script>
    <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/fullscreen.js.下载"></script>
    <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/script.js.下载"></script>

    </html>"""
    return html_content
    
def get_sample_html():
    content = """
    <!DOCTYPE html>
    <html lang="en" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb#">

    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">


      <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">
      <!-- The above 3 meta tags must come first in the head; any other head content comes after -->

      <title>Mood light | Screensaver for chillaxing, meditation, sleeping</title>
      <meta name="description" content="Color changing ambient mood lights - nice place to slow down and relax.">
      <meta name="keywords" content="ocean sound, relaxation">
      <meta name="robots" content="index,follow">
      <link rel="canonical" href="https://defonic.com/moodlight.html">

      <!-- For IE 11, Chrome, Firefox, Safari, Opera -->
      <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-16x16.png" sizes="16x16" type="image/png">
      <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-32x32.png" sizes="32x32" type="image/png">
      <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-96x96.png" sizes="96x96" type="image/png">
      <link rel="icon" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/favicon-192x192.png" sizes="192x192" type="image/png">
      <link rel="apple-touch-icon" sizes="57x57" href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-57x57.png">
      <link rel="apple-touch-icon" sizes="152x152"
        href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-152x152.png">
      <link rel="apple-touch-icon" sizes="180x180"
        href="https://g2k7z4f8.ssl.hwcdn.net/img/fav/apple-touch-icon-180x180.png">

      <meta property="og:url" content="https://defonic.com/moodlight.html">
      <meta property="og:type" content="website">
      <meta property="og:title" content="Mood light">
      <meta property="og:description" content="Screensaver for chillaxing, meditation, sleeping.">
      <meta property="og:image" content="https://defonic.com/screensaver/tw.jpg">


      <!-- Google fonts -->
      <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="">

      <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/reset.min.css">
      <link rel="stylesheet"
        href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/font-awesome.min.css">
      <link href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/css" rel="stylesheet">
      <!-- Ensemble style.css + loader.css -->
      <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style.css">
      <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style(1).css">
      <link rel="stylesheet" href="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/style(2).css">
      
    </head>

    <body onload="initClock()" data-pagenote="1" data-version="4.0.5" data-settings-changed-at="0" data-cid="1707904580053">

      <svg viewBox="0 0 200 100" preserveAspectRatio="xMidYMid slice">
        <defs>
          <radialgradient id="Gradient1" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="34s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255, 0, 255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255, 0, 255, 0)"></stop>
          </radialgradient>
          <radialgradient id="Gradient2" cx="50%" cy="50%" fx="10%" fy="50%" r=".5">
            <animate attributeName="fx" dur="23.5s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255, 255, 0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255, 255, 0, 0)"></stop>
          </radialgradient>
          <radialgradient id="Gradient3" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="21.5s" values="0%;3%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0, 255, 255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0, 255, 255, 0)"></stop>
          </radialgradient>

          <radialgradient id="Gradient4" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="23s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0, 255, 0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0, 255, 0, 0)"></stop>
          </radialgradient>
          <radialgradient id="Gradient5" cx="50%" cy="50%" fx="10%" fy="50%" r=".5">
            <animate attributeName="fx" dur="24.5s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(0,0,255, 1)"></stop>
            <stop offset="100%" stop-color="rgba(0,0,255, 0)"></stop>
          </radialgradient>
          <radialgradient id="Gradient6" cx="50%" cy="50%" fx="50%" fy="50%" r=".5">
            <animate attributeName="fx" dur="25.5s" values="0%;5%;0%" repeatCount="indefinite"></animate>
            <stop offset="0%" stop-color="rgba(255,0,0, 1)"></stop>
            <stop offset="100%" stop-color="rgba(255,0,0, 0)"></stop>
          </radialgradient>
        </defs>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient1)">
          <animate attributeName="x" dur="20s" values="25%;0%;25%" repeatCount="indefinite"></animate>
          <animate attributeName="y" dur="21s" values="0%;25%;0%" repeatCount="indefinite"></animate>
          <animatetransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="17s"
            repeatCount="indefinite"></animatetransform>
        </rect>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient2)">
          <animate attributeName="x" dur="23s" values="-25%;0%;-25%" repeatCount="indefinite"></animate>
          <animate attributeName="y" dur="24s" values="0%;50%;0%" repeatCount="indefinite"></animate>
          <animatetransform attributeName="transform" type="rotate" from="0 50 50" to="360 50 50" dur="18s"
            repeatCount="indefinite"></animatetransform>
        </rect>
        <rect x="0" y="0" width="100%" height="100%" fill="url(#Gradient3)">
          <animate attributeName="x" dur="25s" values="0%;25%;0%" repeatCount="indefinite"></animate>
          <animate attributeName="y" dur="26s" values="0%;25%;0%" repeatCount="indefinite"></animate>
          <animatetransform attributeName="transform" type="rotate" from="360 50 50" to="0 50 50" dur="19s"
            repeatCount="indefinite"></animatetransform>
        </rect>



      </svg>

      <script type="text/javascript">
        function toggle_visibility(id) {
          var e = document.getElementById(id);
          if (e.style.display == 'block')
            e.style.display = 'none';
          else
            e.style.display = 'block';
        }
      </script>

      <div id="timedate">
        <a id="mon">February</a>
        <a id="d">14</a>,
        <a id="y">2024</a><br>
        <a id="h">18</a> :
        <a id="m">04</a> :
        <a id="s">24</a>
      </div>
      <style>
        #timedate {
        position: fixed;
        top: 10px;
        right: 10px;
        display: none;
        font: small-caps lighter 43px/150% "Segoe UI", Frutiger, "Frutiger Linotype", "Dejavu Sans", "Helvetica Neue", Arial, sans-serif;
        text-align:left;
        width: 50%;
        margin: 40px auto;
        color:#A09FA3;
        border-left: 3px solid #A09FA3;
        padding: 20px;
    }
      <style>
      <!-- <p class="calm">relaxed<br><br><a href="http://hipstersound.com/ambience.html"><img src="screensaver/img/hipstersound.png" width="290" height="25" style="opacity:0;" id="logo" alt="more sounds"></a></p>
    -->

      <div class="btnblock">
        <button class="button time" onclick="toggle_visibility(&#39;timedate&#39;);"></button>
      </div>

      <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/jquery.min.js.下载"></script>
      <script type="text/javascript"
        src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/share.js.下载"></script>
      <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/fullscreen.js.下载"></script>
      <script src="./Mood light _ Screensaver for chillaxing, meditation, sleeping_files/script.js.下载"></script>

    </html>
    """
    return content
  
def html_login():
	html = """
	<!DOCTYPE html>
	<html>
	<head>
	<style>
	h1 { 
	display: block;
	font-size: 24px;
	margin-top: 0.67em;
	margin-bottom: 0.67em;
	margin-left: 0;
	margin-right: 0;
	font-weight: bold;
	}

	h2 { 
	display: block;
	font-size: 1.5em;
	margin-top: 0.83em;
	margin-bottom: 0.83em;
	margin-left: 0;
	margin-right: 0;
	font-weight: bold;
	}

	</style>
	</head>
	<body>

	<h1 style="text-align:center;font-size:30px;margin-top:20px">EMIND--音乐生成与推荐系统</h1>
	<!-- <h2 style="text-align:center;font-size:20px">音乐生成与推荐系统</h2> --> 
	<hr>
	<h3 style="text-align:center" >登录</h3>
	"""
	return html

