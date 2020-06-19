#json크롤링.py

import requests
import json            #json import하기

#custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }

#해당 접속 사이트가 아닌 원본데이터가 오는 url 추적. network에서 가지고 온다.
url = "http://finance.daum.net/api/search/ranks?limit=10"

#장고나 플래스크에서 사용했던 reuest 객체 
req = requests.get(url, headers = custom_header)    #custom_header를 사용하지 않으면 접근 불가
print(req.status_code)
if req.status_code == 200:    
    print("접속 성공")
    stock_data = json.loads(req.text)        #json에 반환된 데이터가 들어가 있다.
    for rank in stock_data['data']:         #stock_data는 'data' key값에 모든 정보가 들어가 있다.
        print(rank['rank'], rank['symbolCode'], rank['name'], rank['tradePrice'])

else:
    print("Error code")