from pydoc import classname
import weakref
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import time
from bs4 import BeautifulSoup as Soup
import numpy as np
import csv
import requests
import pandas as pd

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('C:/Users/acer/Desktop/python/chromedriver.exe')        

url = 'https://www.facebook.com' 
driver.get(url)
re = requests.get(url)
re.encoding = 'utf-8'

#帳號密碼
username = 'kpiece82@gmail.com'
password = 'kpiece19930525'

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element(By.ID,"email")
elem.send_keys(username)
elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)        
elem.send_keys(Keys.RETURN)
time.sleep(3)

#要爬的頁面
spec_url = 'https://www.facebook.com/TrueVoiceofTaiwan/posts/pfbid0Mu3KTk5hGZMdtqX6ctPVGticeDAhDiRpjDKYvEv6pTgHwhmaWjVfUfuhWpMnMyXil'
driver.get(spec_url)
time.sleep(2)
def scroll(scrolltimes):
  for i in range(scrolltimes):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(1)

#存貼文內容的陣列
commentlist=[] 

#定位貼文框
soup = Soup(driver.page_source,'html.parser')
time.sleep(2)

comments=soup.find_all("div",class_="xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs")
# scroll(5)
time.sleep(2)
for i in comments:
    c=i.find_all("div",dir="auto")
    if len(c):
        for cc in c:
            print(cc.text)
            commentlist.append(cc.text)
            time.sleep(1.5)
print(commentlist)
time.sleep(1.5)
df = {'comment':[]}
for c in commentlist:
    df['comment'].append(c)
    time.sleep(0.5)
df = pd.DataFrame.from_dict(df) # 直的
time.sleep(2)
df.to_csv("crawler29.csv",index = False,encoding='utf-8-sig')
