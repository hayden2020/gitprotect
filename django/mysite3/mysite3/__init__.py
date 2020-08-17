# file: mysite3/_init_.py
import pymysql
# 让Django 用PYMYSQL 对mysql 服务器进行操作
pymysql.install_as_MySQLdb()