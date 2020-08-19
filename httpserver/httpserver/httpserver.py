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

# 和web frame 通讯的函数
def connect_frame(env):
    s=socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return True
    # 将字典转换为json
    data = json.dumps(env)
    # 将解析后的请求发送给web frame
    s.send(data.encode())
    # 接受来自webframe数据
    data = s.recv(4096 * 100).decode()
    return json.loads(data)  # json.load 表示转化


#将httpserver 基本功能封装为类

class HTTPServer:
    def __init__(self):
        self.address=ADDR   # 从配置文件中获取到地址
        self.create_socket()  #和浏览器交互
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd=socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)


    #绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip=self.address
        self.port=self.address[1]

    # 启动服务器
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        # 多进程并发
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
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'  #正则表达式
        try:
            env=re.match(pattern,request).groupdict()
        except:
            # 客户端断开
            connfd.close()
            return
        else:
            data=connect_frame(env)
            if data:
                self.response(connfd,data)

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




# 代码启动程序
httpd=HTTPServer()
httpd.serve_forever()