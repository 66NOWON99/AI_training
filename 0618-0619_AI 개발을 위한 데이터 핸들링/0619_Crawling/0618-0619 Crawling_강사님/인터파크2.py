from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import pandas as pd 

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)

driver.implicitly_wait(3)

#보통 - 객체를 만들어서 객체반환받아서 쓰는데 
url = "http://tour.interpark.com/"

keyword=input("키워드를 입력하세요")

driver.get(url)


search_box = driver.find_element_by_name("SearchGNBText")
search_box.send_keys(keyword)
"""
#서버로 정보를 전송하는 방법
1. submit 호출
2. enter key 보내기 
3. 직접 자바스크립트 이벤트 중에 click 이벤트를 발생시킨다 

name : find_element_by_name 
id : find_element_by_id
class : find_element_by_class_name
"""
driver.find_element_by_class_name("search-btn").click()

#해외여행 탭 선택하기 
driver.find_element_by_id("li_R").click()

import time
#time.sleep(3)#3초정도 지연시간 
#페이지 이동이 자바스크립트 함수인 searchModule.SetCategoryList(3, '')를 호출한다 
#execute_script : 자바스크립트 함수 호출하기 
#driver.execute_script( "searchModule.SetCategoryList(4, '')")
print("페이지 이동")

"""
searchModule.SetCategoryList(1, '')
searchModule.SetCategoryList(2, '')
searchModule.SetCategoryList(3, '')
searchModule.SetCategoryList(4, '')
"""

from bs4 import BeautifulSoup

dataFrame = pd.DataFrame() 
for i in range(1, 2):
    s = "searchModule.SetCategoryList({}, '')".format(i)
    time.sleep(3)  #초단위 
    driver.execute_script(s) #페이지 옮겼고 
    html = driver.page_source#그 페이지 가져오고 
    bs = BeautifulSoup(html, 'html.parser') #문서 파싱 
    boxItems = bs.findAll("li", {"class":"boxItem"})
    for boxItem in boxItems:
        #print(boxItem)
        title = boxItem.find("h5", {"class":"proTit"}).text
        sub_title = boxItem.find("p", {"class":"proSub"}).text
        #strip - 문자열 앞뒤에 쓸데없는 공백을 지울때 사용한다 
        price = boxItem.find("strong", {"class":"proPrice"}).text.replace("원~", "").strip()
        tour_period = boxItem.findAll("p", {"class":"proInfo"})[0].text
        start_time = boxItem.findAll("p", {"class":"proInfo"})[1].text

        #print(title, sub_title, price, tour_period, start_time)
        dataFrame = dataFrame.append({"title":title, "subTitle":sub_title, 
        "price":price.replace(",",""), 
        "tour_period":tour_period,
        "start_time":start_time}, ignore_index=True)

#print( dataFrame)

for i in range(0, len(dataFrame)):
    print( dataFrame.iloc[i]["title"], 
           dataFrame.iloc[i]["subTitle"], 
           dataFrame.iloc[i]["price"],
           dataFrame.iloc[i]["tour_period"]
           )

dataFrame.to_csv("data.csv", index=False, encoding="CP949")

