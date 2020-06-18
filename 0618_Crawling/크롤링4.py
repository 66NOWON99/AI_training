
url = "http://www.pythonscraping.com/exercises/excercise11utml"

from urllib.request import urlopen1
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import sys

def getTitle(url):
    try:
        html = urlopen(url)
        doc = html.read()
    except HTTPError as e:
        print(e)
        return None #전달해 줄 값이 없다
    
    try: #파싱 에러
        bsObj = BeautifulSoup(doc, 'html.parser')
        title = bsObj.body.h1 #계층형으로 body태그 내의 첫번째 h1태그 지정
        return title
    except AttributeError as e:
        return None

title = getTitle(url)
if title == None:
    print("Title cannot be found ")
else:
    print(title.text)

print(getTitle(url))

