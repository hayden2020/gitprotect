"""
数据库操作模块
思路：
  将数据库操作封装一个类，将dict_server需要i的数据库操作
  功能分别写成方法，在dict_server中实例化对象，
  需要什么方法直接调用
"""
import pymysql

class Database:
    def __init__(self,host='localhost',
                 port=3306,
                 user='root',
                 passwd='123456',
                 charset='utf8',
                 database=None):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.database=database
        self.charset=charset
        self.connect_database()  # 连接数据库
    #连接数据库
    def connect_database(self):
            self.db=pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    passwd=self.passwd,
                                    database=self.database,
                                    charset=self.charset)

    #关闭数据库
    def close(self):
         self.db.close()
    # 创建游标
    def create_cursor(self):
        self.cur=self.db.cursor()

    #注册操作
    def register(self,name,passwd):
        sql="select * from user where name='%s' "%name
        self.cur.execute(sql)
        r=self.cur.fetchone()
        # 查找到则用户存在就返回False
        if r:
            return False
        # 不存在则插入数据库
        sql="insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False


