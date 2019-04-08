import pandas as pd
import numpy as np
#默认索引参数
a=pd.Series([9,8,7,6])
print(a)
#自定义索引
b=pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b)

pd.read_csv()
pd.read_json()
pd.read_hdf()
pd.read_excel()
pd.read_pickle()
pd.to_pickle()

