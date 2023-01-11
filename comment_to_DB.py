#import套件
from asyncio.windows_events import NULL
from csv import reader
from distutils.util import execute
from importlib.resources import path
from sqlite3 import Cursor
from mysql.connector import Error
# -*- coding:utf-8 -*-
import pandas as pd
import csv
import pymysql

db_conn = pymysql.connect(host='127.0.0.1',database='fakenews',user='root',password='1234')
cursor=db_conn.cursor()

with open('./crawler2.csv',newline='',encoding="utf-8-sig") as csvfile:
    rows = csv.reader(csvfile)
    new_list=[]
    for i in rows:
        number=i[0]
        content=i[1]
        #要找post_id
        tup=(number,content,None,None,None,None,None,2)
        new_list.append(tup)
        #改資料表名稱
    insert="insert into comment(comment_number,comment_content,sentence_count,comment_p_value,comment_h_value,count_false,count_true,post_id) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.executemany(insert, new_list)
    db_conn.commit()
cursor.close()