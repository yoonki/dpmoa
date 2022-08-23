# %%
import requests
from bs4 import BeautifulSoup
import json
import datetime
import pandas as pd
from urllib.request import urlopen
import ssl
import urllib3
import time
from selenium import webdriver
from tqdm import tqdm
import schedule
import streamlit as st

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()
pd.set_option('display.max_colwidth', 100)

# %%
url = 'https://m.bunjang.co.kr/shop/4860292/products'
response = requests.get(url, verify=False)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# %%
tilte = soup.find_all('div', 'sc-bfYoXt.eAzkkl')

# %%
tilte

# %%

options = webdriver.ChromeOptions()
# mobile_emulation = { "deviceName": "iPhone X" }
options.add_argument('headless')

# options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome('/Users/yoonkilee/Documents/chromedriver', options=options)


# %%
url ='https://m.bunjang.co.kr/shop/4860292/products'
driver.get(url)

# driver.set_window_size('1080', '1920')      #the trick
# time.sleep(2)
# driver.save_screenshot("00screenshot.png")


# %%
products = driver.find_elements_by_css_selector('#root > div > div > div.sc-eQGPmX.kYBVAE > div > div.sc-cSYcjD.fVHGdp > div.sc-eweMDZ.entwBX > div.sc-cnTzU.iXfzew > div.sc-cmIlrE.jmiReu > div.sc-fKGOjr.fALQdp > div > a')
titles = driver.find_elements_by_css_selector('#root > div > div > div.sc-eQGPmX.kYBVAE > div > div.sc-cSYcjD.fVHGdp > div.sc-eweMDZ.entwBX > div.sc-cnTzU.iXfzew > div.sc-cmIlrE.jmiReu > div.sc-fKGOjr.fALQdp > div > a > div.sc-eAKXzc.brUNPn > div.sc-bfYoXt.eAzkkl')
prices = driver.find_elements_by_css_selector('#root > div > div > div.sc-eQGPmX.kYBVAE > div > div.sc-cSYcjD.fVHGdp > div.sc-eweMDZ.entwBX > div.sc-cnTzU.iXfzew > div.sc-cmIlrE.jmiReu > div.sc-fKGOjr.fALQdp > div > a > div.sc-eAKXzc.brUNPn > div.sc-gkFcWv.dOnitE')

# %%
url_list = []
title_list = []
price_list = []
for i in range(len(titles)):
    title_list.append(titles[i].text)
    try:
        price_list.append(prices[i].text)
    except:
        price_list.append(prices[i].text)

datas = {'상품명' : title_list, '가격' : price_list}
    


# %%
dpmoa = pd.DataFrame(datas)

# %%
dpmoa



