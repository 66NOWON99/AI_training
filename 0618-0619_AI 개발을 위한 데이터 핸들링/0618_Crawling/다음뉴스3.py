"""
다음뉴스3.py


https://search.daum.net/search?w=news&DA=PGD&spacing=0&p=3&q=%EC%BD%94%EB%A1%9C%EB%82%98
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse #한글 깨짐 문제 해결

search ="&q" + parse.quote_plus("코로나")
page = "&page=1"

url = "https://search.daum.net/search?w=news&DA=PGD&spacing=0&p=3" + search + page
print(url)

html = urlopen(url) #연결작업
html_doc = html.read() #문서읽기 
# print(html_doc)
bs = BeautifulSoup(html_doc)
div = bs.find("div", {"class": "compo-fulltext ty_tit2"})
li = div.ul.findAll("li")
liList = div.ul.findAll("li")
for item in liList:
    print(item.find("strong",{"class":"tit-g"} ).text)