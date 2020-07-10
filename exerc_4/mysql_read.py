#倒入模块
import pymysql
#连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   database='stu',
                   user='root',
                   password='123456',
                   charset='utf8')
#获取游标
cur=db.cursor()

#数据库操作
sql="select * from class where id=1"
cur.execute(sql)
one_row=cur.fetchone()
print(one_row)  #元组

