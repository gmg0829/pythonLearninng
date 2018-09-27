import pandas as pd
#默认索引参数
a=pd.Series([9,8,7,6])
print(a)
#自定义索引
b=pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b)