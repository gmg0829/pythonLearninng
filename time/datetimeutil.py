from datetime import datetime,timedelta
a=datetime.now()
#date转换为timestamp
b=a.timestamp()
#timestamp转换为date
t = 1429417200.0
#print(datetime.fromtimestamp(t))
#str转换为date
str='2015-12-1 16:15:00'
c=datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
#print(c)
#date转换为str
d=a.strftime('%Y-%m-%d %H:%M:%S')
#print(d)
f=a+timedelta(days=1)
print(f)
