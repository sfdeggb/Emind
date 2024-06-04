def default_lyric_template():
	result=""
	with open("template/lyric_template.txt", "r",encoding="utf-8") as f:
		content = f.readlines()
		for i in range(len(content)):
			content[i] = content[i].replace("\n", "").replace("，", "").replace("。", "").replace("？", "").replace("！", "").replace(" ","")
			result+=content[i]
	return result

if __name__ == "__main__":
	print(default_lyric_template())