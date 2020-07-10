import pymysql

#连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

#获取游标（操作数据库，执行sql语句）
cur=db.cursor()


#执行SQL语句
sql=("insert into class values(5,'glass',77.7,'2020-7-6');")
cur.execute(sql)
db.commit()

cur.close()
db.close()