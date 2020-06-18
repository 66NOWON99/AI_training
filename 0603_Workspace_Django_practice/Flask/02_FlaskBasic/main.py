#module
from flask import Flask

#서버를 생성한다.
#Flask 객체를 생성하면 서버가 생성되고 이를 이용해
#서버를 가동하면 된다.
#Flask 객체를 만들 때 문자열 아무거나 넣어주면 된다.
#보통 __name__을 넣어준다.
app = Flask(__name__)

#브라우저 요청 정보에 따라 처리하는 부분
#return 하는 문자열이 브라우저로 전달된다.

#주소만 입력했을 경우
@app.route("/")
def index():
    return 'Hello World'

#주소 뒤에 test를 붙였을 경우
@app.route('/test')
def test():
    return 'Hello Test'
#서버 가동
#host : 브라우저가 요청할 때 사용할 ip주소
#현재 서버 역활을 할 컴퓨터의 IP주소를 넣어주면 된다.
#port : 브라우저가 사용할 포트번호
#포트번호는 컴퓨터에서 프로그램을 구분하기 위한 수단입니다.
#debug : True를 넣어주면 파일 수정시 서버가 자동으로 다시 가동된다.
#개발시에만 설정한다.
#가독성,!

#host에다 내 컴퓨터의 ip를 입력해보자  (cmd->ipconfig)로 ip를 알 수 있다
app.run(host='192.168.1.145', port='80',debug=True) #port=80은 자동으로 붙여져서  눈에안보임













