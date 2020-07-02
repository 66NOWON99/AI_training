#해외축구.py

import requests
import json 

url = "https://sports.media.daum.net/sports/record/epl/team?season=20192020"
url="https://media.daum.net/proxy/hermes/api/team/rank.json?leagueCode=epl&seasonKey=20192020&page=1&pageSize=100"
req = requests.get(url)

print( req.status_code)
if req.status_code==200:
    data = json.loads(req.text)
    #string -> 파이썬 개체 형태로 전환한다 
    print( '현재 페이지 : ', data['pagingInfo']['page'])
    print( '페이지 크기: ', data['pagingInfo']['pageSize'])

    teamList = data['list']
    for team in teamList:
        print(team['nameMain'], team['nameKo'], team['shortNameKo'], 
        team["rank"]["rank"],  team["rank"]["game"],  team["rank"]["win"],
         team["rank"]["draw"])