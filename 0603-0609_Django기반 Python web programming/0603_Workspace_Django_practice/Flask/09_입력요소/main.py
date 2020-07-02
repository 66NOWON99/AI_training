from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/test1',methods=['post'])
def test1() :
    data1 = request.values.get('data1')
    data2 = request.values.get('data2')
    data3 = request.values.get('data3')
    data4 = request.values.get('data4')

    # 같은 이름으로 여러개가 전달될 경우~getlist(multiple select, checkbox)
    # data5=x,data=y...와 같은 값들을 list로 묶음
    data5 = request.values.getlist('data5')

    data6 = request.values.get('data6')
    data7 = request.values.getlist('data7')
    return f'''
            <h4>data1 : {data1}</h4>
            <h4>data2 : {data2}</h4>
            <h4><pre>data3 : {data3}</pre></h4>
            <h4>data4: {data4}</h4>
            <h4>data5: {data5}</h4>
            <h4>data6: {data6}</h4>
            <h4>data7: {data7}</h4>
            '''
#  pre: 입력된 문자를 그래도 출력해줌 (pre없으면 엔터쳤을 때 스페이스로 나옴)


app.run(host="192.168.1.145",port=80,debug=True)