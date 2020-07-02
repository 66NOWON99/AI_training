

"""
다음뉴스.py
https://news.v.daum.net/v/20200618154305031
<h3 class="tit_view" data-translation="">'모범형사' 손현주 연기, 벌써 美쳤다</h3>
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://news.v.daum.net/v/20200618154305031"

html = urlopen(url) #연결작업
html_doc = html.read() #문서읽기

bsObj = BeautifulSoup(html_doc, 'html.parser') #파싱
title = bsObj.find("h3",{"class": "tit_view"})
print("기사제목 : ", title.txt)