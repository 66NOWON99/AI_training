"""
아이리포.py
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ilifo.co.kr/center"

html = urlopen(url) #연결작업
html_doc = html.read() #문서읽기
"""
class="info_image"
"""

bs = BeautifulSoup(html_doc, 'html.parser') #파싱
divList = bs.findAll("div", {"class":"info_image" })
liList = divList[0].ul.findAll("li")
for li in liList:
    img = li.img
    print(img['src'])





