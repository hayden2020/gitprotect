from socket import *
#创建套字节
sockfd=socket(AF_INET,SOCK_DGRAM)

#绑定地址
ADDR=('127.0.0.1',888)

#循环收发信息
while True:
    data=input("Msg>>")  #输入信息
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)#发送信息
    msg,addr=sockfd.recvfrom(1024)#接受消息
    print("From Server:",msg.decode())
sockfd.close()