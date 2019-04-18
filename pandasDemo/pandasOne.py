import pandas as pd
import numpy as np
#默认索引参数
a=pd.Series([9,8,7,6])
print(a)
#自定义索引
b=pd.Series([9,8,7,6],index=['a','b','c','d'])
print(b)

# pd.read_csv()
# pd.read_json()
# pd.read_hdf()
# pd.read_excel()
# pd.read_pickle()
# pd.to_pickle()

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
obj.drop(['d', 'c'])

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four',
                             'five', 'six'])
frame2.loc['three']
frame2['debt'] = 16.5
del frame2['debt']
