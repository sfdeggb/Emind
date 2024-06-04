import os
import time
import pymysql
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db_connection import create_connection

# 创建数据库连接
conn = create_connection('localhost', 3306, 'root', '123456', 'music_rec')
cursor = conn.cursor()

# 用户ID
user_id = '00003a4459f33b92906be11abe0e93efc423c0ff'

# 序号开始值
seq_num = [7]

# 目录路径
dir_path = '/root/muzic/musicagent/public/audios'

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        # 只处理文件，忽略目录
        if not event.is_directory:
            # 获取文件路径
            file_path = event.src_path

            # 获取文件创建时间
            file_create_time = os.path.getctime(file_path)
            # 转换为可读的时间格式
            file_create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file_create_time))

            # 插入到数据库
            cursor.execute(
                "INSERT INTO music_gen (seq_num, file_path, file_create_time, user_id) VALUES (%s, %s, %s, %s)",
                (str(seq_num[0]).zfill(4), file_path, file_create_time, user_id)
            )

            # 序号递增
            seq_num[0] += 1

            # 提交到数据库执行
            conn.commit()

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=dir_path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# 关闭数据库连接
cursor.close()
conn.close()