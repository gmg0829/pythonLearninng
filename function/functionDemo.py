import math
from functools import reduce
from operator import itemgetter
def area(width,height):
    return width * height
#print(area(2,4))
def add(a,b,f):
    return f(a)+f(b)
c=add(2,-5,abs)
#print(c)
k=[1,2,3,4]
#print(list(map(str,k)))
def f(n):
    return n*n
list1=[1,2,3,4]
#print(list(map(f,list1)))
def add1(x,y):
    return  x+y
list2=[2,3,4,5]
#print(reduce(add1,list2))
#print(sum(list2))
def fn(x,y):
    return  x*10+y
list3=[1,2,3,4]
#print(reduce(fn,list3))
def isodd(n):
    return n%2==1
list4=[2,3,4,5,6,7]
#print(list(filter(isodd,list4)))
def no_empty(n):
    return n and n.strip()
list5=['2',' ','3','',None]
#print(list(filter(no_empty,list5)))
list6=[-2,3,-5,8]
#print(sorted(list6,key=abs))
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

#print(sorted(students, key=itemgetter(0)))
#print(sorted(students, key=lambda t: t[1]))
#print(sorted(students, key=itemgetter(1), reverse=True))
std1={'name':'gmg','score':95}
def print_score(std):
    print('名字是%s,分数为%s' %(std['name'],std['score']) )
print_score(std1)
