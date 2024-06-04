import pymysql

def create_connection(host, port, user, password, db):
    try:
        connection = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

if __name__ =="__main__":
    conn = create_connection('localhost', 3306,
                          'root', 
                          '123456', 
                          'music_rec')
    print(conn)