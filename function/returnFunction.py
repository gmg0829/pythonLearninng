def calc_sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
#print(calc_sum(2,3,4,5))
#可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,4,5)
#print(f())

