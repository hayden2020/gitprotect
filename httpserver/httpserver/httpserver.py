"""
httpserver 主程序
将请求发送给Web Frame
从Web Frame接受反馈数据
将数据组织为Reasponse格式大佛嗯给客户端
"""
from socket import *
import sys,re,json
from threading import Thread
from config import *

# 服务器地址
ADDR=(HOST,PORT)

#将httpserver 基本功能封装为类

class HTTPServer:
    def __init__(self):
        self.address=ADDR
        self.create_socket()  #和浏览器交互
        self.connect_socket()  #连接web frame
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    #创建和web frame 交互的套接字
    def connect_socket(self):
        self.connect_socket=socket
        frame_addr=(frame_ip,frame_port)
        try:
            self.connect_socket.connect(frame_addr)
        except Exception as e:
            print(e)
            sys.exit()




    #绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip=self.address
        self.port=self.address[1]

    # 启动服务器
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            connfd,addr=self.sockfd.accept()
            print("Connect from ",addr)
            client=Thread(target=self.handle,args=(connfd,))
            client.setDaemon(True)
            client.start()

        #具体处理客户端请求任务
    def handle(self,connfd):
        # 获取HTTP请求
        request = connfd.recv(4096).decode()
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'
        try:
            env=re.match(pattern,request).groupdict()
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            # 将字典转换为json
            data=json.dumps(env)
            #将解析后的请求发送给web frame
            self.connect_socket.send(data.encode())
            # 接受来自webframe数据
            data=self.connect_socket.recv(4096*100).decode()
            self.response(connfd,json.loads(data))    #json.load 表示转化

        #给浏览器发送数据
        def response(self,connfd,data):
            if data['status']=='200':
                responseHeaders="HTTP/1.1 200 OK\r\n"
                responseHeaders+="Content-Type:text/html\r\n"
                responseHeaders+='\r\n'
                responseBody=data['data']
            elif data['status']=='404':
                responseHeaders = "HTTP/1.1 404 not Found\r\n"
                responseHeaders+= "Content-Type:text/html\r\n"
                responseHeaders += '\r\n'
                responseBody = data['data']

            # 给浏览器发送数据
            response_data=responseHeaders+responseBody
            connfd.send(response_data.encode())





httpd=HTTPServer()
httpd.serve_forever()