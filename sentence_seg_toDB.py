import re
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

def cut_sentences(content):
	sentences = re.split(r'\.|\!|\?|。|！|，|？|\.{6}', content)
	return sentences

content = content = '中介法推了以後，我一定票投國民黨！因為我好想看民進黨作繭自縛的窘樣！下架綠是唯一選項！也可能是綠轉移林智堅焦點戰術！若讓綠勝選，選後一定強推！'
sentences = cut_sentences(content)
new_list=[]
count=0
for i in sentences:
    s=[i]
    count=count+1
    tup=(count,s,None,None,2)
    new_list.append(tup)
insert="insert into sentence(sentence_number,sentence_content,sentence_p_value,sentence_h_value,source_comment_id) values(%s,%s,%s,%s,%s)"
cursor.executemany(insert, new_list)
db_conn.commit()

# print('\n'.join(sentences)) #幫你轉成string
# print(new_list)

cursor.close()
