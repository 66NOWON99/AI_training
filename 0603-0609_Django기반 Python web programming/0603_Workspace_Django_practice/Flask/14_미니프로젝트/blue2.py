# blue2.py
from flask import Blueprint, render_template, request
from db import db_connect

content_blue = Blueprint('content_blue', __name__, template_folder='content_template')

@content_blue.route('/test2')
def test2() :
    return render_template('test2.html')

# 토론방 내용 페이지
@content_blue.route("/content_main/<topic_idx>")
def content_main(topic_idx) :

    # 데이터베이스 접속
    conn = db_connect()

    # 토론 주제 가져오기
    sql1 = '''
            select topic_subject
            from topic_table
            where topic_idx = ?
           '''

    data1 = [topic_idx]

    cursor1 = conn.cursor()
    cursor1.execute(sql1, data1)
    result1 = cursor1.fetchone()
    # row 1개만 나오는 건 fetchone (ex; 방 번호는 중복 될 수 없기에 fetchone)
    # row 여러개는 fetchall

    #글 내용 가져오기
    # content_txt: 글 내용
    sql2 = '''
            select content_text
            from content_table
            where content_topic_idx = ?  
            order by content_idx
            '''
    cursor2 = conn.cursor()
    cursor2.execute(sql2, data1)
    result2 = cursor2.fetchall()

    conn.close()

    return render_template('content_main.html',topic=result1, topic_idx=topic_idx, content_list=result2)
# return //컨텐츠, 토픽, 방번호

# 글 작성 처리
@content_blue.route('/add_content_pro', methods=['post'])
def add_content_pro() :
    # 데이터 추출
    topic_idx = request.values.get('topic_idx')
    topic_content = request.values.get('topic_content')

    #데이터베이스 접속
    conn = db_connect()

    #autoincrement 붙은 것 빼고쓰기
    sql = '''
            insert into content_table (content_topic_idx, content_text)
            values (?, ?)
          '''

    data = [topic_idx, topic_content]
    conn.execute(sql, data)
    conn.commit()
    conn.close()

    return f'''
            <script>
                alert('저장되었습니다')
                location.href = 'content_main/{topic_idx}'
            </script>
           '''

