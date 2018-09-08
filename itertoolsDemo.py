import  itertools
#无限迭代器
naturls=itertools.count(1)
#for i in naturls:
#    print(i)
cs=itertools.cycle('ABC')
#for i in cs:
#    print(i)
c=itertools.repeat('acx',10)
for i in c:
    print(i)
