from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime 
import pandas as pd 
import time 
import re 

#화면 스크롤 작업을 해야 한다 
scroll_pause_time =0.5 
". : 내가 작동중인 경로, 상대경로 지정   ..:내 부모 "
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA/")

#화면 전체를 가져와서 크기정보로 스크롤을 하기 위해서 body태그 객체를 가져온다
#find_element_by_tag_name - 태그를 갖고 오고자 할때 
body = driver.find_element_by_tag_name("body")

#반복적으로 진행한다, 언제 끝날지 몰라서 무한루프로 진행한다 
def scroll_screen(cnt):
    i=1
    while True: 
        #현재 화면의 길이를 알아온다 
        last_height = driver.execute_script(
            "return document.documentElement.scrollHeight")
        print(last_height)
        #스크롤하기 
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_pause_time)
        #Keys - 키보드의 값들을 - 약속되어 있는 상수값 , enter key:RETURN
        i=i+1
        if i>=cnt:
            break 

#함수호출 
scroll_screen(5)
html = driver.page_source
bs = BeautifulSoup(html, "html.parser")
#print(html)

"""
titleList = bs.findAll("a", {"id":"video-title"})
print(titleList[0]['aria-label'])
print(titleList[0]['title'])
"""
divList = bs.findAll("div", {"id":"dismissable", 
             "class":"style-scope ytd-grid-video-renderer"})
for video in divList:
    title = video.find("a", {"id":"video-title"})
    viewcnt = video.find("span", 
        {"class":"style-scope ytd-grid-video-renderer"})
    if title != None:
        print(title.text, viewcnt.text)



"""
id="video-title" class="yt-simple-endpoint style-scope 
ytd-grid-video-renderer" 
aria-label="식당에서 나오는 바로 그 '콘치즈'! Corn Cheese! A Dish of Peculiar Charm 게시자: 백종원의 요리비책 Paik's Cuisine 22시간 전 10분 47초 조회수 316,257회" 
title="식당에서 나오는 바로 그 '콘치즈'! Corn Cheese! A Dish of Peculiar Charm" href="/watch?v=zS_o6psOt9g">식당에서 나오는 바로 그 '콘치즈'! Corn Cheese! A Dish of Peculiar Charm</a>
<span class="style-scope ytd-grid-video-renderer">조회수 31만회</span>

"""
