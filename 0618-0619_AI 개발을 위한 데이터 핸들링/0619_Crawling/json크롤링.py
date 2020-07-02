import requests
import json            #json import하기

#custom_header을 통해 아닌 것 처럼 위장하기
custom_header = {
    'referer' : 'http://http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }

#해당 접속 사이트가 아닌 원본데이터가 오는 url 추적. network에서 가지고 온다.
url = "http://finance.daum.net/api/search/ranks?limit=10"

#장고나 플라스크에서 사용했던 request 객체
req = requests.get(url, headers = custom_header)    #custom_header를 사용하지 않으면 접근 불가
print( req.status_code )

if req.status_code == 200: #200:정상접속    
    print("접속 성공")
    stock_data = json.loads(req.text)        #json에 반환된 데이터가 들어가 있다.
    for rank in stock_data['data']:         #stock_data는 'data' key값에 모든 정보가 들어가 있다.
        print(rank['rank'], rank['symbolCode'], rank['name'], rank['tradePrice'])

else:
    print("Error code")

# 접속 성공
# 1 A001000 신라섬유 2350
# 2 A068270 셀트리온 211500
# 3 A048410 현대바이오 12650
# 4 A005930 삼성전자 44650
# 5 A207940 삼성바이오로직스 338500
# 6 A020560 아시아나항공 6460
# 7 A002210 동성제약 20150
# 8 A007460 에이프로젠 KIC 4000
# 9 A066570 LG전자 77000
# 10 A000660 SK하이닉스 80200