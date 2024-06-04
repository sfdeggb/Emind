import logging 

def create_logging(logger_name, log_name):
    # 创建一个logger
	logger = logging.getLogger(logger_name)
	logger.setLevel(logging.DEBUG)  # 设置日志级别
	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler(log_name)
	fh.setLevel(logging.DEBUG)

	# 创建一个handler，用于输出到控制台
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# 定义handler的输出格式
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	
	# 给logger添加handler
	logger.addHandler(fh)
	logger.addHandler(ch)

	return logger 
