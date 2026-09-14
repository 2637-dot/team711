import pymysql
conn = pymysql.connect(host="localhost", user='root', password="q1w2e3", db="shopping_db")
cur = conn.cursor()
cur.execute("select * from CUSTOMER")
result = cur.fetchall()
print(result)

cur.close()
conn.close()
