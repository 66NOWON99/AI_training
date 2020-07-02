#workshop#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import pandas as pd

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)

driver.implicitly_wait(3)

#보통 - 객체를 만들어서 객체반환받아서 쓰는데 
url = "https://www.ilifo.co.kr/boards/chunsik"

driver.get(url)

import time
time.sleep(2) #2초 시간지연

for i in range(1,4):
    s = "pageCallback({},''); return false;".format(i)
    time.sleep(2) #초단위
    driver.execute_script(s) #페이지 옮겼고
    html = driver.page_source #옮긴 페이지 가져오고
    bs = BeautifulSoup(html,'html.parser') #문서파싱 ; in for loop-page마다 파싱이 이뤄져야함

   
    tbody = bs.find("tbody")
    trList = tbody.findAll("tr")

    for tr in trList:
        tdList = tr.findAll("td")
        for td in tdList:
            print(td.text, end=' ')
        print()
    