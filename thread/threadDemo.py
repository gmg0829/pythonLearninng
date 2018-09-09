import _thread,time
#为线程第一一个函数
def print_time(threadname,delay):
    count=0
    while count<5:
        count+=1
        print("%s:%s"%(threadname,time.ctime(time.time())))
#创建两个线程
try:
    _thread.start_new_thread(print_time,("thread1",2))
    _thread.start_new_thread(print_time,("thread2",4))
except:
    print("无法启动线程")
while 1:
    pass