
def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 4, 7])
for i in x:
     print(i)   

def multiplier_func(a, b):
    return a * b

y= map(multiplier_func, [1, 4, 7], [2, 5, 8])
for i in y:
     print(i)      