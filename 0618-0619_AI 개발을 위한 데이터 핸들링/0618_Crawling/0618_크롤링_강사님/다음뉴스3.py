"""
다음뉴스3.py

https://m.search.daum.net/search?w=news&DA=PGD&n=15&page=3&q=%EC%BD%94%EB%A1%9C%EB%82%98
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse  #한글깨짐문제 해결

search = "&q="+ parse.quote_plus("코로나")

for i in range(1, 6):
    page = "&page="+str(i)  #i - int 타입 -> string타입으로 전환된다. 

    url = "https://m.search.daum.net/search?w=news&DA=PGD&n=15"+ search + page
    print(url)

    html= urlopen(url) #연결작업
    html_doc = html.read() #문서읽기 
    #print(html_doc)
    bs = BeautifulSoup(html_doc)
    div = bs.find("div", {"class":"compo-fulltext ty_tit2"})
    liList = div.ul.findAll("li")
    for item in liList:
        print(item.find("strong", {"class":"tit-g"}).text) 

"""
과제:토요일 자정까지 : 본인이름 - 소스 

https://www.ilifo.co.kr/boards/chunsik?page.page=2&searchType=title&searchWord=
번호 제목 작성자 작성일 댓글수 조회수 

littleconan@hanmail.net 

192.168.1.116
"""