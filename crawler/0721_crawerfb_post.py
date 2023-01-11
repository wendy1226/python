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
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)

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
spec_url = 'https://www.facebook.com/nuliapp'
driver.get(spec_url)
time.sleep(2)
def scroll(scrolltimes):
  for i in range(scrolltimes):
    js = 'window.scrollTo(0, document.body.scrollHeight);'
    driver.execute_script(js)
    time.sleep(1)

#存貼文內容的陣列
post=[] 

#定位貼文框
x1=driver.find_elements(By.CLASS_NAME,'du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0') 
time.sleep(2)
i = 0
while i < 791:
  print("length")
  print(len(x1))
  print("i=" + str(i))
  print(x1[i])

  try:
    #先判斷有沒有內文
    time.sleep(1)
    getpost=x1[i].find_element(By.XPATH,'.//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"]')
    #print(getpost.text)
    try:
      #再判斷有沒有按鈕
      time.sleep(1)
      post_more=x1[i].find_elements(By.CLASS_NAME,"oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id.lrazzd5p")[1]
      print(post_more.text)
      time.sleep(1.5)
      #按下顯示更多按鈕
      x1[i].find_element(By.XPATH,".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m']//div[@role='button']").click()
      #取得貼文內容
      time.sleep(0.5)
      getpost=x1[i].find_element(By.XPATH,'.//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"]')
      #把貼文內容加進去post[]裡
      time.sleep(0.5)
      post.append(getpost.text)
      time.sleep(0.5)
      print(getpost.text)
    except:
      time.sleep(1)
      getpost=x1[i].find_element(By.XPATH,'.//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"]')
      post.append(getpost.text)
    #這邊是例如他只是換封面照片或是發圖片，沒有貼文文字的情況下，就直接在post[]存"沒有內文"
  except:
    post.append("沒有內文")
  time.sleep(0.5)
  driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
  x2=driver.find_elements(By.CLASS_NAME,'du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0') 
  print(len(x2))
  x1=x2
  i=i+1
  time.sleep(1)
print(post)


df = {'post':[]}
for p in post:
    df['post'].append(p)
df = pd.DataFrame.from_dict(df) # 直的
df.to_csv("post.csv",index = False,encoding='utf-8-sig')
