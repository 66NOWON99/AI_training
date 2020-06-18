from flask import Flask, render_template
#템플릿 폴더 경로를 지정하지 않았기 때문에 render_template 함수 사용시
#templates 폴더에서 파일을 찾는다.
# app = Flask(__name__)

#템플릿 폴더 경로를 지정했기 때문에 render_template 함수 사용시
#지정된 폴더에서 파일을 찾는다
app=Flask(__name__,template_folder='views')

@app.route("/")
def index():
    # return 'Hello World'
    # return '<h1>Hello World</h1>'
    # return '''
    #         <html>
    #             <body>
    #             </head>
    #                 <meta charset = 'utf-8'/>
    #             </head>
    #             <body>
    #                 <h1>Hello World</h1>
    #                 a href = 'http://google.com'>구글</a>
    #             <.body>
    #         <html>
    #         '''
    #지정된 템플릿 폴더 안에 있는 html파리
    return render_template('index.html')



app.run(host='192.168.1.145',port=80, debug=True)