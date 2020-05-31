import numpy
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from dotenv import load_dotenv
import os

load_dotenv()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(r"C:\Users\Lenovo\Desktop\fb-crawler\chromedriver.exe", chrome_options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.facebook.com/groups/IB.fanpage.club/")

FACEBOOK_ACCOUNT = os.getenv("FACEBOOK_ACCOUNT")
FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")
driver.find_element_by_id("email").send_keys(FACEBOOK_ACCOUNT) # 將USERNAME改為你的臉書帳號
driver.find_element_by_id("pass").send_keys(FACEBOOK_PASSWORD) # 將PASSWORD改為你的臉書密碼
driver.find_element_by_id("loginbutton").click()
time.sleep(3)
sp = BeautifulSoup(driver.page_source, 'html.parser')
# print(sp)


# 貼文
POST = []
post = sp.find_all(class_="text_exposed_root")
for i in post:
    POST.append(i.text)
print(POST)
print(len(POST))

# 貼文時間
POST_TIME = []
post_time = sp.find_all("abbr")
for i in post_time:
    if i.get("title") != None:
        POST_TIME.append(i.get("title"))
print(POST_TIME)
print(len(POST_TIME))

# 貼文者
POSTER = []
poster = sp.find_all(class_='fwn fcg')
for i in poster:
    if i.a.get("title") != None:
        POSTER.append(i.a.get("title"))
print(POSTER)
print(len(POSTER))

# 頭像
PHOTO = []
photo = sp.find_all(class_='_38vo')
for i in photo:
    PHOTO.append(i.img['src'])
print(PHOTO)
print(len(PHOTO))

# 讚總數
likes = []
likes_ammount = sp.find_all(class_="_81hb")
for i in likes_ammount:
    likes.append(int(i.text.replace(",", "")))
print(likes)
print(len(likes))

# 留言總數
comments = []
comments_ammount = sp.find_all(class_="_3hg- _42ft")
for i in comments_ammount:
    comments.append(int(i.text.replace("則留言", "")))
print(comments)
print(len(comments))


# 創建一個折線圖專用csv檔案
import csv

fb = open("line_chart.csv", "w", encoding="utf-8-sig")
csv_writer = csv.writer(fb)
csv_writer.writerow(["貼文時間", "讚總數"])
for i in range(len(POST)):
    csv_writer.writerow([POST_TIME[i], likes[i]])
fb.close()

# 使用pandas讀取CSV檔
import pandas as pd
df = pd.read_csv(r'C:\Users\Lenovo\Desktop\fb-crawler\line_chart.csv')
print(df)

# 使用matplotlib繪製折線圖
from matplotlib import pyplot as plt
plt.plot(df["讚總數"])
plt.show()




