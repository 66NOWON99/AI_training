from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)

driver.implicitly_wait(3)

#보통 - 객체를 만들어서 객체반환받아서 쓰는데 
url = "http://tour.interpark.com/"
keyword="도쿄"

driver.get(url)


search_box = driver.find_element_by_name("SearchGNBText")
search_box.send_keys(keyword)

"""
#서버로 정보를 전송하는 방법
1. submit 호출
2. enter key 보내기
3. 직접 자바스크립트 이벤트 중에 click 이벤트를 발생시킨다

name : find_element_by_name
id  : find_element_by_id
class : find_element_by_class_name
"""
#검색 버튼 클릭하기
driver.find_element_by_class_name("search-btn").click()

#해외여행 탭 선택하기
driver.find_element_by_id("li_R").click()

import time
time.sleep(2) #2초 시간지연

#페이지 이동이 자바스크립트 함수인 searchModule.SetCategoryList(3, '')를 호출한다
#execute_script : 자바스크립트 함수 호출하기
driver.execute_script("searchModule.SetCategoryList(3, '')")
print("페이지 이동")

"""
searchModule.SetCategoryList(1, '')
searchModule.SetCategoryList(2, '')
searchModule.SetCategoryList(3, '')
searchModule.SetCategoryList(4, '')
"""
for i in range(1,5):
    s = "searchModule.SetCategoryList({}, '')".format(i)
    print(s)
    time.sleep(1)
    driver.execute_script(s)
#.format() //숫자와 문자를 결합할 때 사용

# from bs4 import BeautifulSoup
# html = driver.page_source
#print(html)
