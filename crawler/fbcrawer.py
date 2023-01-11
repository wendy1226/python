# selenium
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver # 載入需要的套件
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.action_chains import ActionChains
import re, time, requests 

#from pandas.core.frame import DataFrame

import time
import pandas as pd


# ------ 設定要前往的網址 ------
url = 'https://www.facebook.com'  

# ------ 登入的帳號與密碼 ------
username = 'w19981226@yahoo.com.tw'
password = 'mkh9826mkh'


# ------ 透過Browser Driver 開啟 Chrome ------
driver = webdriver.Chrome('C:/Users/acer/Desktop/python/chromedriver.exe')        

# ------ 前往該網址 ------
driver.get(url)        

# ------ 賬號密碼 ------
# time.sleep(1)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element(By.ID,"email")
elem.send_keys(username) # 傳入字串

elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)      

elem.send_keys(Keys.RETURN)
time.sleep(5)

# 切換頁面
spec_url = 'https://www.facebook.com/ChooseBetterHsinchu/posts/pfbid02u9vXdh2SDUMsxuKGpJYkcX99isYKnBVGrQRBUzhyjMfn87pA3q49EH3PEuH6Bm1ql'
#'https://www.facebook.com/New27Brigade/posts/pfbid0AAVLonoL965RRiBXsJ9u4uoK8QUyjBQJM9PTFmSMrpnoz8PxQ481KYnY7eRrvpg3l'

driver.get(spec_url)
time.sleep(5)

contents = []
savecomment = []

# 將網頁元素放入Beautifulsoup
soup = Soup(driver.page_source,"html.parser")

# 往下滑3次，讓Facebook載入文章內容 
for x in range(4):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    time.sleep(10)

# 定位文章標題
titles = soup.find_all(
    "div", class_="ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a")

for title in titles:
    # 定位每一行標題
    posts = title.find_all("div", dir="auto")
    # 如果有文章標題才印出
    if len(posts):
        for post in posts:
            print(post.text)
            contents.append(post.text)

    print("-" * 30)

#可用的爬留言
comments=soup.find_all("div",class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql")
for comment in comments:
    c=comment.find_all("div",dir="auto")
    if len(c):
        for cc in c:
            print(cc.text)
            savecomment.append(cc.text)

collect_fb = pd.DataFrame()

df = {'comment':[]}
for c in savecomment:
    df['comment'].append(c)
    time.sleep(0.5)
df = pd.DataFrame.from_dict(df) # 直的
time.sleep(2)
df.to_csv("comment1.csv",index = False,encoding='utf-8-sig')


