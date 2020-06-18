from bs4 import beautifulSoup

html_doc = open("./test3.html", encoding="utf8")
s = html_doc.read()

bs = beautifulSoup(s)

table = bs.find("table")
print(table)

#thead쪽에 있는 제목들
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
        print(td.text, end=" ")
        # end= " " ; 줄바꿈이 아니라 옆으로 차례대로 나온다
    print()

#다른 방법으로
print("자식 객체로 가져오기")
for child in table.thead.children: 
    print(child.get_text() )
