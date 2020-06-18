
print("크롤링")
print("쉬는시간 주세요")

#ctrl - ~: 터미널 창이 보였다 안보였다
#ctrl F5 : 실행
#터미널 창에서 python test1.py
 
from urllib.request import urlopen
"""
문서를 요청했을 때 상태정보 숫자
200 성공적
400 문서 없음 - url이 잘못되었다
500 사이트 오류
"""


html = urlopen("http://www.daum.net")
s = html.read()
print(s)

url = "http://www.pythonscraping.com/exercises/exercise1.html"
html = urlopen(url)
s = html.read()
pring(s)

#파싱용 라이브러리
from bs4 import BeautifulSoup
bs = BeautifulSoup(s) # html 문서를 전달하면서 객체 생성하기 - 파싱 완료


print("파싱하기")
div = bs.findAll("div") #배열로 받아온다
print (div[0]. text)

