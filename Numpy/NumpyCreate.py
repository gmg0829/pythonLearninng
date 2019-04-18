# 使用array创建数组：
arr = np.array([1,2,3]) --创建一维数组
arr = np.array([1,2,3],[4,5,6],[7,8,9])  --创建二维数组
# 使用arange创建数组
arr = np.arange(0,10,1)  --创建初值为0，终值为9的递增一维数组
arr = np.arange(12).reshape(3,4) --创建1-12的3行4列的二维数组
# 使用linspace创建等差数组
arr = np.linspace(0,10,1)
# 使用logspace创建等比数组
arr = np.logspace(0,2,20)
# 使用zeros创建元素全为0的数组
arr = np.zeros((2,3)) --创建2行3列的二维数组
# 使用eye创建对角线元素为1的单位矩阵
arr = np.eye(3)
# 使用diag创建对角线元素为0或其他的矩阵
arr = np.diag([1,2,3,4])
# 使用ones创建元素全为1的数组
arr = np.ones((4,3))



np.random.random(100)  --生成100个0-1的随机数
np.random.rand(10,5)   --生成10行5列0-1的服从均匀分布的随机数
np.random.randn(10,5)  --生成正态分布的随机数
np.random.randint(2,10,size = [2,5])  --生成2行5列取值为2-10整数的随机数



# 一维数组的索引，与Python中list的索引方式一致
arr[5], arr[3:5], arr[:5], arr[-1], arr[1:-1:2]--2表示隔一个元素取一个

# 二维数组的索引：arr[1:,2:],各个维度的索引用逗号隔开


# 改变数组形状--reshape
arr.reshape(3,4) 改为3行4列
# 使用ravel展平数组--横向展平
arr.ravel()
# 使用flatten横向或纵向展平数组
arr.flatten() ---横向展平
arr.flatten('F')  ---纵向展平
# 数组横向组合--hstack()
np.hstack((arr1,arr2))
# 数组的纵向组合 --vstack()
np.vstack((arr1,arr2))
# 数组的横向分割--hsplit
np.hsplit(arr,2)
# 数组的纵向分割--vsplit
np.vsplit(arr,2)


# 数组的四则运算：
x = np.array([1,2,3])
y = np.array([4,5,6])
x + y
x - y
x * y
x / y
x ** y
# 数组之间的比较
x < y
x > y
x == y
x != y  --输出为bool值


# 对数组继续排序
arr.sort(axis =1) --沿着横轴排序
arr.sort(axis =0) --沿着纵轴排序
# 对数组进行去重
np.unique(arr)
# 数组的重复--tile
np.tile(arr,3)
# 数组中每个元素进行重复--repeat
arr.repeat(2,axis=0)--按行进行元素重复
arr.repeat(2,axis=1)--按列继续元素重复
# 常用的统计函数
sum()
max()
min()
mean()
std()
var()
cumsum() --累计和
cumprod  --累计积
