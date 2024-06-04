import gradio as gr 
from gradio import themes
from html_c.gradio_html import get_index_html

with gr.Blocks(theme="default") as demo:
  index_html = get_index_html()
  gr.HTML(index_html)
  gr.Textbox("Text", type="text", label="Input Text")

with gr.Blocks(theme=themes.Base(primary_hue=themes.colors.whole_white)) as demo1:
  index_html = get_index_html()
  gr.HTML(index_html)
  gr.Textbox("Text", type="text", label="Input Text")
  
if __name__ == "__main__":
  demo.launch(server_port=8081)
	