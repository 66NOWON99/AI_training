
"""
다음뉴스.py
https://news.v.daum.net/v/20200618152226982
<h3 class="tit_view" data-translation="true">입주 하루 앞둔 새 아파트에 물 새고 벽에 금 가고</h3>
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://news.v.daum.net/v/20200618152226982"

html = urlopen(url) #연결작업
html_doc = html.read() #문서읽기

bsObj = BeautifulSoup(html_doc, 'html.parser') #파싱
title = bsObj.find("h3",{"class": "tit_view"})
print("기사제목 : ", title.txt)

section = bsObj.find("section")
print(section)

pList = section.findAll("p")
for ptag in pList:
    print(ptag.text)

p = section.find("p", {"dmcf-pid": "jmt00iu0hl"})
print("***")
print(p)

