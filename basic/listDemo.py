hello = (1, 2, 3)
li = [1, "2", [3, 'a'], (1, 3), hello]
li.append("pytaya")
li.insert(0,'balabala')
li.pop()
li.pop(0)
li.remove('2')
#访问元素
print(li[3],li[-2])
#切片访问
#格式: list_name[begin:end:step]begin 表示起始位置(默认为0)，end 表示结束位置(默认为最后一个元素)，step 表示步长(默认为1)
print(li[0:2],li[:2])
print(li[0:3:2])
#嵌套访问
print(li[-2][1])
#删除元素
del li[3]
print(li)
#操作符
# + 用于合并列表
# * 用于重复列表元素
# in 用于判断元素是否存在于列表中
# for ... in ... 用于遍历列表元素
a=[1,2,3]+[4,5,6]
print(a)
print(a*2)
print(7 in a)
for k in a:
    print(k)
#len(list) 列表元素个数 max(list) 列表元素中的最大值 min(list) 列表元素中的最小值 list(seq) 将元组转换为列表
#https://mp.weixin.qq.com/s?__biz=MjM5ODE1NDYyMA==&mid=2653387604&idx=1&sn=3dbac8356f723f31e927cd3382d33a19&chksm=bd1cc3478a6b4a517dcf7ef86aeeb327be64104c60ad2d5c2438208cb0a32161e3779684a421&mpshare=1&scene=1&srcid=0912pOM35RxmK8SrPLwvPn5Q#rd


