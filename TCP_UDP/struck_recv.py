from socket import *
import struct
#和客户端一致
st=struct.Struct('i32sif')

#udp套接字
s=socket(AF_INET,SOCK_DGRAM)
s.bind(( '127.0.0.1',8888))

#打开文件
f=open('student.txt','a')
while True:
     data,addr=s.recvfrom(1024)#接收数据
     data=st.unpack(data)

     #写入文件
     info="%d  %-10s  %d  %.1f\n"%data
     f.write(info)
     f.flush()