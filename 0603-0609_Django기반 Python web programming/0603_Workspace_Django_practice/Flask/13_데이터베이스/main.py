from flask import Flask, render_template, request
# sqlite 용 모듈
# sqlite3.dll, sqlite3.def 파일을
# c:\windows\system32 폴더에 복사해 넣어줘야 한다.
import sqlite3

app = Flask(__name__)

# 데이터 베이스 접속 함수
def get_connection():
    conn = sqlite3.connect('test.db')

    # (쿼리문) 테이블이 없을 경우 테이블을 만든다.
    sql ='''
            create table if not exists flasktable(
                data1 int not null,
                data2 int not null,
                data3 int not null
            );
         '''
    conn.execute(sql)
    conn.commit()

    return conn

@app.route('/')
def index():
    # conn = get_connection()
    # conn.close()
    return render_template('index.html')

@app.route("/add", methods=['post'])
def add() :
    # 클라이언트가 보낸 데이터 추출
    data1 = request.values.get('data1')
    data2 = request.values.get('data2')
    data3 = request.values.get('data3')

    # 쿼리문 생성 (값이 들어갈 부분은 ?로 작성한다)
    sql = '''
            insert into flasktable (data1, data2, data3)
            values (?, ?, ?)  
          '''
    # 데이터 베이스 접속 함수를 호출
    conn = get_connection()
    # # 쿼리문 관리 객체를 추출한다.
    # cursor = conn.cursor()
    # # 쿼리문을 실행한다.
    # cursor.execute(sql,(data1, data2, data3))
    #insert, update, delete
    #select 같은 경우엔 cursor가 필요함. 그렇지않은 경우엔 사용할 필요x

    conn.execute(sql,(data1, data2, data3))

    conn.commit()

    conn.close()

    return '저장완료'

@app.route('/show')
def show():
    #데이터베이스 접속
    conn = get_connection()
    # 쿼리문
    sql = '''
            select data1, data2, data3
            from flasktable
          '''
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    #fetchall: 각 리스트의 데이터가 넘어옴 (각 컬럼의 데이터가 리스트로 넘어옴)

    conn.close()
    # print(result)
    return render_template('show.html', result=result)


app.run(host="192.168.1.145",port=80,debug=True)
