#크롤링2.py
"""
로컬 경로에서 html 문서를 읽어 파싱하기 
"""
from bs4 import BeautifulSoup

html_doc = open("./test2.html", encoding="utf8")
s = html_doc.read()
print(s)

#파싱 - 읽어들인 xml문서를 BeautifulSoup 객체 전달한다 
bs = BeautifulSoup(s) #bs가 문서 읽어서 파싱한 정보를 가지고 있다 
#태그명만 주면 첫번째꺼 하나만 찾는다 
h1 = bs.find("h1")
print(h1) #h1객체 자체를 출력한다 
print(h1.text) #태그를 제외한 text 만 추출하기

#같은 태그가 여러개 있을때 배열로 찾는 방법 find_all 
hList = bs.find_all("h1")
print( hList[0].text)
print( hList[1].text)
print( hList[2].text)

for title in hList:
    print( title.text )

p = bs.find("p")
print("p", p.text)

#태그로 접근하기 - find, find_all 태그명 
#모든 태그에는  id, class 속성이 있다 
"""
id - 한 페이지에서 아이디는 중복되면 안된다. javascript에서 태그에 접근할때
     이 속성의 값을 이용해서 접근하는데, 중복이 되면 접근을 할 수 가 없다 
class - 여러개의 태그가 동일한 클래스명을 소유할 수 있다.배열의 형태 
     보통 화면의 디자인등을 주기 위해 사용하는 속성이다 

input, textarea 태그는 별도로 name 속성을 가질 수 있는데 name 속성에 
값을 담아서 서버로 전송할때 사용한다.  배열의 형태로 데이터가 전달된다. 
배열로 접근할 수 있다.
html 파싱시 태그뿐만 아니라 이 세개의 속성을 이용해서 값을 적당하게 가져올 
수 있다 
"""
#첫번째인자로 태그명, 두번째 인자 id속성명 
tag = bs.find("h1", id="blue1")
print( tag.text )

tag = bs.find("h1", id="blue2")
print( tag.text )

for i in range(1,3):
    tag = bs.find("h1", id="red"+str(i))
    print(tag.text)

#class 속성 사용시 find_all 을 쓰자 
tags = bs.find_all("h1",class_="blueclass")
for tag in tags:
    print( tag.text )

#파라미터를 dict타입으로 전달한다. 
tags = bs.find_all("h1",{"class":"blueclass"})
for tag in tags:
    print( tag.text )

id = bs.find("h1", {"id":"red1"})
print(id.text)

#ul태그에 대한 참조를 먼저 얻는다
ul1 = bs.find("ul", {"class":"coffee"})
print(ul1.find("li").text)
for li in ul1.findAll("li"):
    print(li.text)

ul1 = bs.find("ul", {"class":"jucy"})
print(ul1.find("li").text)
for li in ul1.findAll("li"):
    print(li.text)

