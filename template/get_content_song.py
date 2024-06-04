import random 

def get_contend_id(description=""):
	with open("template/song_content.txt", "r", encoding="utf-8") as f:
		content = f.readlines()
		for i in range(len(content)):
			content[i] = content[i].replace("\n", "")
		id = random.choice(content)
	return id

if __name__=="__main__":
	print(get_contend_id())