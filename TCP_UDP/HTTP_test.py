from socket import *
s=socket()
s.bind(('0.0.0.0',8003))
s.listen(3)
c,addr=s.accept()
print("Connect from ",addr)
data=c.recv(4096)#接受HTTP的请求
print(data)
response="""HTTP/1.1 200 OK
Content-Type:text/html
Hello World
"""
c.send(response.encode()) #发送响应的内容
c.close()
s.close()