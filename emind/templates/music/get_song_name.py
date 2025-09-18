import random 

def song_name(description=""):
	with open("template/sample_song_chinese.txt", "r",encoding="utf-8") as f:
		content = f.readlines()
		for i in range(len(content)):
			content[i] = content[i].replace("\n", "")
		#从列表中随机选取一首歌
		song = random.choice(content)
	return song

if __name__ == "__main__":
	print(song_name())
