# Flask : 웹서버 기능을 하기위한 클래스
# render_template : html 파일을 통해 응답 결과를 만드는 함수
# request : 브라우저가 전달하는 요청정보를 관리하는 객체
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test1')
def test1() :
    # 요청방식이 get 방식일 경우
    # 요청 파라미터 : a1=100 & a2=200 & a3=300
    a1 = request.args.get('a1')
    a2 = request.args.get('a2')
    a3 = request.args.get('a3')

    return f'''
            <h3>a1 : {a1}</h3>
            <h3>a2 : {a2}</h3>
            <h3>a3 : {a3}</h3>
            '''

@app.route('/test2',methods=['post'])
def test2():
    # post 방식일 경우 데이터를 추출
    v1 = request.form.get('v1')
    v2 = request.form.get('v2')
    v3 = request.form.get('v3')

    return f'''
            <h3>v1 : {v1}</h3>
            <h3>v2 : {v2}</h3>
            <h3>v3 : {v3}</h3>
            '''

@app.route('/test3',methods=['get','post'])
def test3():
    # get, post 구분하지 않고 데이터를 추출한다.
    data1 = request.values.get('data1')
    data2 = request.values.get('data2')
    data3 = request.values.get('data3')

    return f'''
            <h3>data1 : {data1}</h3>
            <h3>data2 : {data2}</h3>
            <h3>data3 : {data3}</h3>
            '''

app.run(host="192.168.1.145",port=80,debug=True)

