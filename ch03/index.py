from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<num>")
def up(num):
    print(num)
    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결
        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study2')
    cur = conn.cursor()
    sql = "INSERT INTO numcount (num) VALUES (%s)"
    cur.execute(sql, (num,))
    conn.commit()
    conn.close()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)



