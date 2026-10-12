import pymysql

class LED:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            db='study2',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor  # 선택사항: 결과를 딕셔너리 형태로 반환
        )
        self.cur = self.conn.cursor()
        print("connect ok!! good")

    def get(self):
        query = "SELECT * FROM record_led"
        self.cur.execute(query)
        results = self.cur.fetchall()
        print(results)
        return results

    def save(self, status):
        # %s 파라미터 전달 방식을 사용 (tuple 형태)
        query = "INSERT INTO record_led (status) VALUES (%s)"
        self.cur.execute(query, (status,))
        self.conn.commit()
        print(f"Saved status: {status}")


