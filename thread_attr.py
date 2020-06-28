from threading import Thread
from time import sleep
def fun():
    sleep(3)
    print("线程属性测试")
t=Thread(target=fun,name='hayden')

t.setName(True)  #主线程退出分支线程也退出

t.start()

t.setName('dhn')
print("name:",t.getName())
print("is alive:",t.is_alive())
print("daemon:",t.daemon)