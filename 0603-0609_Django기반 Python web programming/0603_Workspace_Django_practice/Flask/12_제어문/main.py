from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():

    list1 = [10, 20, 30, 40, 50]

    return render_template('index.html', a1=10, a2=list1)

app.run(host="192.168.1.145",port=80,debug=True)