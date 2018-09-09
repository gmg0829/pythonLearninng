#关闭文件第一种方式
try:
    f=open('gmg.txt','r')
    f.read()
finally:
    if f:
        f.close()
#关闭文件第二种方式
with open('gmg.txt','r') as d:
    d.read()
