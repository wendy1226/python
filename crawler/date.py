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
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)

url = 'https://www.facebook.com' 
driver.get(url)
re = requests.get(url)
re.encoding = 'utf-8'

#帳密
username = 'w19981226@yahoo.com.tw'
password = 'walleyeknee1226starlove'

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element(By.ID,"email")
elem.send_keys(username)
elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)        
elem.send_keys(Keys.RETURN)
time.sleep(3)

#要爬的頁面
spec_url = 'https://www.facebook.com/nuliapp'

driver.get(spec_url)
time.sleep(3)
def scroll(scrolltimes):
  for i in range(scrolltimes):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(1)

#存貼文內容的陣列
date=[] 

#定位貼文框
x1=driver.find_elements(By.CLASS_NAME,'du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0') 

time.sleep(2)

i = 0
while i < 791:
    print("lengh")
    print(len(x1))
    print("i=" + str(i))

    print(x1[i])
    try:
        #滑鼠移到日期
        #move_to_date=x1[i].find_element(By.XPATH,'.//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 m9osqain"]')
        move_to_date=x1[i].find_element(By.XPATH,'.//span[@class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"]')
        ActionChains(driver).move_to_element(move_to_date).perform()
        time.sleep(1)
        try:
        #取得日期內容
            getdate=driver.find_element(By.XPATH,'//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh e9vueds3 j5wam9gi b1v8xokw oo9gr5id hzawbc8m"]').text
        except:
            getdate=x1[i].find_element(By.XPATH,'//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]').text
    except:
        date.append("0")
    print(getdate)
    time.sleep(0.5)
    #把貼文內容加進去post[]裡
    date.append(getdate)
    driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    x2=driver.find_elements(By.CLASS_NAME,'du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0') 
    print(len(x2))
    x1=x2
    i=i+1
    time.sleep(1)
print(date)


df = {'date':[]}
for p in date:
    df['date'].append(p)
time.sleep(1)
df = pd.DataFrame.from_dict(df) # 直的
time.sleep(1)
df.to_csv("date.csv",index = False,encoding='utf-8-sig')











