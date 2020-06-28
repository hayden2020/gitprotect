filename=input("File:")
try:
    fr=open(filename,'rb')#二进制打开
except FileNotFoundError as e:
    print(e)
else:
    fw=open(test1.py,'wb')#二进制写入
    while True:
        data=fr.read(1024)
        if not data:      #文件结束
            break
        fw.write(data)    #将读取内容写入
    fr.close()
    fw.close()
