def foo1():
    a=5 #局部作用域
    print(a)
foo1()

b=10 #全局作用域
def foo2():
    print(b)
foo2()

def foo3():
    global c;
    c=3
    print(c)
foo3()
print(c)