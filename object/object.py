class myClass:
    i=1
    def a(self):
       return "你好"
x=myClass()
#print(x.i)
#print(x.a())
class my:
    def __init__(self,a,b):
        self.t=a
        self.u=b
y=my(1,3)
#print(y.t)
#print(y.u)
class Student:
    def __init__(self,name,score):
        self._name=name
        self._score=score
    def print_score(self):
        print('%s,%s' %(self._name,self._score))
b=Student('gmg',100)
#b.print_score()
#print(b._name)
class Animal():
    def run(self):
        print("animal is running")
class Dog(Animal):
    pass
dog=Dog()
dog.run()