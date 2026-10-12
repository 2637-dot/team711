#db제어

import pymysql

class TodoDB:
    def __init__(self):
        #1. 디비 연결
        self.conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study2')
        self.cur = self.conn.cursor()
        print("connect ok")
    def get(self):
        #모든 태스크 가져오기
        #쿼리 작성
        sql = "select * from todos"
        self.cur.execute(sql)
        values = self.cur.fetchall()
        return values
    def add(self, title):
        #title을 todos 테이블에 넣기
        sql = "insert into todos(task) into values('{title}')"
        self.cur.execute(sql)
        self.conn.commit()
    def remove(self, todo_index):
        sql = f"delete from todos where todo_index = {todo_index}"
        self.cur.execute(sql)
        self.conn.commit()

