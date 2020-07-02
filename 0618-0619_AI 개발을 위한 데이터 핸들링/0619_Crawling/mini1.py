from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
# from bs4 import BeautifulSoup
from urllib.request import urlopen
# import pandas as pd
import pyautogui
import requests

print("xx")


def search():
    
    keyword = input("키워드를 입력하세요 : ")

    driver = webdriver.Chrome("./chromedriver.exe")
    # driver.implicitly_wait(3)
    
    url = "https://m.search.naver.com/search.naver?sm=mtb_hty.top&where=m_news"
    
    driver.get(url)
    search_box = driver.find_element_by_id("nx_query")
    search_box.send_keys(keyword)
    pyautogui.press('enter')
    
    titles = driver.find_element_by_class_name('list_news') #전체 페이지
    title = titles.find_elements_by_class_name('news_wrap') #뉴스 별로
    return title
   