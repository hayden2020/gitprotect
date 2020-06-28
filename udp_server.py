from socket import *
#创建套字节
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定地址
server_addr=('127.0.0.1',888)
sockfd.bind(server_addr)
#循环发送消息
while True:
    data, addr=sockfd.recvfrom(1024)
    print("收到消息:",data.decode())
    sockfd.sendto(b'Thanks',addr)
#关闭套字节
sockfd.close()