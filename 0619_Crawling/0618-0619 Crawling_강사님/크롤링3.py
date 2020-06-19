from bs4 import BeautifulSoup

html_doc = open("./test3.html", encoding="utf8")
s = html_doc.read()

bs = BeautifulSoup(s)

table = bs.find("table")
#print(table)

#thead쪽에 있는  제목들 
thead = table.find("thead")
print(thead)

th = thead.findAll("th")
print(th[0].text)
print(th[1].text)
print(th[2].text)

tbody = table.find("tbody")
trList = tbody.findAll("tr") #배열이라서 
for tr in trList:
    tdList = tr.findAll("td")
    for td in tdList:
        print( td.text, end=" ")
    print()

#다른 방법으로 
"""
print("자식객체로 가져오기")
for c in bs.find("table").thead.children: 
    print( c.get_text() )
"""