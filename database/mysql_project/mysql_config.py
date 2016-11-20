import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mydb',
                                       user='root',
                                       password='root',
                                       #port='8889',
                                       # Charset = 'utf8'
                                       )
        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')
        return conn
    except Error as e:
        print(e)

#    finally:
 #       conn.close()
    return conn
if __name__ == '__main__':
    connect()

