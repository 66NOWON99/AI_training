#확장팩 : anaconda, html snippet
#크롤링1.py

from urllib.request import urlopen
"""
문서를 요청했을때 상태정보 숫자 
200 성공적
404 문서 없음 - url이 잘못되었다 
500 - 사이트가 오류
"""
url = "http://www.pythonscraping.com/exercises/exercise1.html"
html = urlopen(url)
s = html.read()
print(s)

#파싱용 라이브러리 
from bs4 import BeautifulSoup
bs = BeautifulSoup(s) # html문서를 전달하면서 객체 생성하기 - 파싱 완료

print("파싱하기")
div = bs.findAll("div") #배열로 받아온다 
print( div[0].text) 








