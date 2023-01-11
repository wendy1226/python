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

driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.facebook.com' 
driver.get(url)
re = requests.get(url)
re.encoding = 'utf-8'
username = 'w19981226@yahoo.com.tw'
password = 'walleyeknee1226starlove'
# ------ 輸入賬號密碼 ------
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element(By.ID,"email")
elem.send_keys(username)
elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)        
elem.send_keys(Keys.RETURN)
time.sleep(3)

# 切換頁面
spec_url = 'https://www.facebook.com/UniigymTW'
driver.get(spec_url)

def scroll(scrolltimes):
  for i in range(scrolltimes):
    # 每一次頁面滾動都是滑到網站最下方
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(1)
    
# 呼叫scroll function，就會直接滾動頁面
scroll(5)

soup = Soup(driver.page_source,'html.parser')
frames = soup.find_all(class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')
df = {'like':[],'comment':[],'share':[]}
post=[]


# 建立一個空的list
like = []
# 抓取每一篇貼文的按讚數
for ii in frames: 
    thumb = ii.find('span',class_="pcp91wgn")
    # 有些貼文沒有按讚數，所以抓下來的東西是None，因此直接append 0
    if(thumb == None): 
        like.append('0')
    else:
        like.append(thumb.text)  
time.sleep(5)
for i in range(len(like)):  
    # 處理出現 '\xa0萬' 的數值
    if(like[i].find('\xa0萬') != -1):
        like[i] = int(float(like[i][:like[i].find('\xa0萬')])*10000)
        
    # 處理有出現 ',' 的數值
    else:
        like[i] = int(like[i].replace(',',''))
time.sleep(5)
print(like)

# 抓取留言數
comment_nums = []
share = []
for ii in frames: 
    lengh=ii.find_all('span',class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain")
    if(len(lengh)==2):
        readComment = lengh[0]
        readShare =lengh[1]
        comment_nums.append(readComment.text)
        share.append(readShare.text)
    elif(len(lengh)==1):
        if "留言" in lengh[0].text:
            readComment = lengh[0]
            comment_nums.append(readComment.text)
            share.append('0次')
        elif "分享" in lengh[0].text:
            readShare =lengh[0]
            share.append(readShare.text)
            comment_nums.append('0則')
# 留言數資料整理
for i in range(len(comment_nums)):
    index = comment_nums[i].find('則')
    comment_nums[i] = int(comment_nums[i][:index].replace(',',''))
print(comment_nums)

for i in range(len(share)):
    index = share[i].find('次')
    share[i] = int(share[i][:index].replace(',',''))
print(share)


for a in like:
    df['like'].append(a)
for b in comment_nums:
    df['comment'].append(b)
for c in share:
    df['share'].append(c)


df = pd.DataFrame.from_dict(df) # 直的
df.to_csv("test.csv", index = False) # 也可以將csv改成xlsx

time.sleep(3)
# 關閉瀏覽器
driver.quit()

