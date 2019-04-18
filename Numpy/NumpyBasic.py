# 数学计算
import numpy as np
my_arr=np.array([[0,1,2,3],[4,5,6,7]])
#数据的维度
print(my_arr.ndim)
#行数和列数
print(my_arr.shape)
#对象元素的个数
print(my_arr.itemsize)
#元素类型
print(my_arr.dtype)
attackdata=np.random.randn(7,4)#对应name随机生成一个7*4的二维数组
print(attackdata)
#矩阵乘法
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[1, 4], [2, 5], [3, 6]])
print(x.dot(y))




