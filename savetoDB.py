
import mysql.connector 
from mysql.connector import Error

try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='127.0.0.1',          # 主機名稱
        database='fakenews', # 資料庫名稱
        user='root',        # 帳號
        password='1234')  # 密碼

    # 更新資料
    sql = "INSERT INTO corpus_c (word,adverb_value) VALUES (%s,%s,%s);"
    new_data = ("是", 0,)
    cursor = connection.cursor()
    cursor.execute(sql, new_data)

    # 確認資料有存入資料庫
    connection.commit()

except Error as e:
    print("資料庫連接失敗：", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
