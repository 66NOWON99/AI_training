"""
다음뉴스.py
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://m.daum.net/"

html = urlopen(url) #연결작업
html_doc = html.read() #문서읽기
"""
class="ta_txt rubics_single"
"""

bs = BeautifulSoup(html_doc, 'html.parser') #파싱
#첫번째거 하나만
tagList = bs.find("li",{"class": "ta_txt rubics_single"})
print(tagList.text)

#목록 다 - 배열로, find_all 또는 findAll
tagList = bs.findAll("li",{"class": "ta_txt rubics_single"})
for i in range(0,len(tagList)): # 배열의 index
    print(tagList[i].text)

for item in tagList:
    print(item.text)

print("속성만 추출하기")
tagList = bs.find("li",{"class": "ta_txt rubics_single"})
a = tagList.find("a") #list 태그에서 anchor 태그 객체 추출하기
print("href: ",a['href']) #태그에서 href 속성값 추출하기


