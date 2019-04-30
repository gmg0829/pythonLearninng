import pandas as pd
import numpy as np
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
#frame.to_csv("data.csv", sep=",", index=False)#数据以逗号分隔，且没有索引
#frame.info() #基础数据集特征信息
#print(frame.describe()) #基础数据集统计结果
#print(frame.columns)#列出列名称

dates = pd.date_range('20130101', periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df.head()
df.tail(3)
df.index
df.to_numpy()
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
df['A']
df[0:3]
df['20130102':'20130104']
df.loc[:, ['A', 'B']]
df.loc['20130102':'20130104', ['A', 'B']]
df[df.A > 0]
df2 = df.copy()
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
#print(df1)
df1.dropna(how='any')
df1.fillna(value=5)
df.mean()#每一列平均值
df.mean(1)#每一行平均值
df.sum()#每一列的和
df.sum(1)#每一行的和

df3 = pd.DataFrame({'key1':['a', 'a', 'b', 'b', 'a'],
    'key2':['one', 'two', 'one', 'two', 'one'],
    'data1':np.random.randn(5),
    'data2':np.random.randn(5)})
df3['data1'].groupby(df3['key1'])    

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
middle=pd.merge(left, right, on='key')
#print(middle)
x=1
y=2
c=True
result=x if c else y
print(result)