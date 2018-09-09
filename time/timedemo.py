import time
a=time.time()
print("当前时间戳",a)
#本地时间
localtime=time.localtime(a)
print("本地时间",localtime)
#格式化本地时间
formatlocaltime=time.asctime(localtime)
print("格式化后的时间为",formatlocaltime)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))