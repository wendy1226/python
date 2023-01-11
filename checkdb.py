from audioop import alaw2lin
from re import A
import mysql.connector 
from mysql.connector import Error
import numpy as np

numpyArray=[]
new = [['wendy','0'],['Alan2','1'],['Alan','1']]
checkedarray=[]

def querytable(a,b):
    for i in a:
        k=0
        for j in b:
            print(i)
            print(j)
            if i[0]==j[0] and i[1]==j[1]:
                new.remove(new[k])
                # print("找到第幾列是重複的:")
                # print(k)
                # checkedarray.append(k)
            k=k+1
                
# 連結 SQL
connect_db = mysql.connector.connect(
        host='127.0.0.1',          # 主機名稱
        database='fakenews', # 資料庫名稱
        user='root',        # 帳號
        password='1234')  # 密碼

with connect_db.cursor() as cursor:
    # sql = """
    # INSERT INTO corpus_a (word, pos, hurt_value,corpus, manual_check) VALUES 
    # ('Alan2',true , 1, "a", true)
    # """

    sql = """
    SELECT word, pos FROM corpus_a
    """
    # 執行 SQL 指令
    cursor.execute(sql)

    data=cursor.fetchall() #取出所有資料

    numpyArray = np.array(data)

    # # 提交至 SQL
    # connect_db.commit()

# 關閉 SQL 連線
connect_db.close()

print("原本的b:")
print(new)

querytable(numpyArray,new)
# for k in checkedarray:
#     print("checkedarray的值:")
#     print(k)
#     new.remove(new[k])
    # np.delete(new,[1], axis=1) #axis=1是列
print("更新後的new陣列:")
print(new)