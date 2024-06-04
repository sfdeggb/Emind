import os 

def count_code_lines(file_path):
	try:
		with open(file_path, 'r', encoding='utf-8',errors="ignore") as f:
			return len(f.readlines())
	except Exception as e:
		print(f"Error reading file: {file_path}")
		return 0

if __name__ =="__main__":
	project_code_lines = 0
 	#os.path.dirname(os.path.abspath(__file__))
	project_dir = "/root/muzic/musicagent/"
	for root, dirs, files in os.walk(project_dir):
		for file in files:
			if file.endswith('.py') or file.endswith('.html') or file.endswith('.css'):
				file_path = os.path.join(root, file)
				if "/root/muzic/musicagent/ui/recommand_system/Lib/site-packages" in file_path:
					continue
				file_count = count_code_lines(file_path)
				print(f"{file_path} has {file_count} lines of code")
				# print(file_path)
				# print(count_code_lines(file_path))
				# print("\n")
				project_code_lines+=file_count
	print(f"Total lines of code: {project_code_lines}")
	print("\n")