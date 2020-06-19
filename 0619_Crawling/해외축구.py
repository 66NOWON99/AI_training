#해외축구.py
from urllib.request import urlopen
import requests
import json  


url = "https://sports.media.daum.net/sports/record/epl/team?season=20192020"
url="https://media.daum.net/proxy/hermes/api/team/rank.json?leagueCode=epl&seasonKey=20192020&page=1&pageSize=100"
req = requests.get(url)

print( req.status_code)
if req.status_code==200:
    data = json.loads(req.text)
    #string -> python 개체 형태로 전환해준다.

    print("현재 페이지 : ",data['pagingInfo']['page'])
    print("페이지 크기 : ",data['pagingInfo']['pageSize'])
    
    teamList = data['list']
    for team in teamList:
        print(team['nameMain'], team['nameKo'], team['shortNameKo'],
        "rank: ", team["rank"]["rank"],"game: ",team['rank']['game'],"win: ",team['rank']['win'],
        "draw: ",team['rank']['draw'])

