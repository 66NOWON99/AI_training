from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import pyautogui
import requests

# pip install pyautogui

# def search():
#     path = "./chromedriver.exe"
#     driver = webdriver.Chrome(path)

#     driver.implicitly_wait(3)
    
#     url = "https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query="
#     # url = "https://m.news.naver.com/"

#     #//
#     # url = "https://m.news.naver.com/search.nhn?searchType=issue"


#     driver.get(url)
#     keyword = input("키워드를 입력하세요 : ")
#     search_box = driver.find_element_by_id("nx_query")
#     search_box.send_keys(keyword)
#     pyautogui.press('enter') 
#     titles = driver.find_element_by_class_name('list_news') #전체 페이지
#     title = titles.find_elements_by_class_name('news_wrap') #뉴스 별로
#     return title
        


    ####################################
        #//
    # search_box = driver.find_element_by_name("query")
    
    
    # driver.find_element_by_class_name("gnb u_hssbt u_hssbt_ss").click()
    
    # <button type="submit" class="gnb u_hssbt u_hssbt_ss" onclick="nclk(event,'gnb.sch','','');">
    # <span class="u_vc">뉴스검색</span></button>

    # <button class="search-btn" type="button" onclick="searchBarModule.ClickForSearch();">검색</button>
    ####################################



def parsing(title):
    
    lst = [] #title

    for tit in title: 
        txt = tit.text.split('\n') 
        txt = txt[2] #제목만 남기기 
        lst.append(txt) 
        #기사 클릭
        #tit.find_element_by_class_name('news_tit').click()
        for target in range: # --> while 문으로
            source = BeautifulSoup(webpage, 'html5lib')
            comments = source.find_all('span', {'class':'desc_review'})
            # 새 탭에서 기사 열기
            target = title.find_element_by_class_name('news_tit')
            target.send_keys(Keys.CONTROL+"\n")
            browser.switch_to.window(browser.window_handles[1])
            # 기사창의 댓글 더보기 클릭 -> 댓글 크롤링
            loading = title.find_element_by_class_name("u_cbox_in_view_comment").click()
            commentList = bsObj.findAll("span",{"class":"u_cbox_contents"})
            for comment in commentList:
                print(comment.get_text())
            # 기사창 닫고 기사 목록 창으로 돌아가기
            browser.close()
            browser.switch_to.window(browser.window_handles[0])


        driver.get(url)
        webpage = urlopen(url)
        source = BeautifulSoup(webpage, 'html5lib')
        comment = source.find('span', {'class':'u_cbox_contents'})
        print(comment)
    print(lst) #제목만 든 리스트

title = search()
parsing(title)

