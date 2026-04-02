import pymysql

# db 연결
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       db = 'tabledb',
                       charset='utf8')
# sql 명령문을 실행하는 객체
cursor = conn.cursor()

sql = 'SELECT * FROM usertbl'
cursor.execute(sql) # 명령문 실행

# 명령문 실행한 결과 행들 출력
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()