"""
web frame.py  模拟后端应用工作流程
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver

"""

from socket import *
import json
from settings import *
from select import select

# 应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind((frame_ip,frame_port))

app=Application()
app.start()    # 启动应用服务


sockfd=socket()
sockfd.bind(('0.0.0.0',8080))
sockfd.listen(3)
while True:
    c,addr=sockfd.accept()
    data=c.recv(1024).decode()
    print(json.loads(data))
    d={'status':'200','data':'xxxxxxxxxxxx'}
    c.send(json.dumps(d).encode())