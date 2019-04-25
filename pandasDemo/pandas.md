```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime
import re

sr.unique             Series去重
sr.value_counts()     Series统计频率，并从大到小排序，DataFrame没有这个方法
sr.describe()         返回基本统计量和分位数

df.describe()         按各列返回基本统计量和分位数
df.count()            求非NA值得数量
df.max()              求最大值
df.min()              求最大值
df.sum(axis=0)        按各列求和
df.mean()             按各列求平均值
df.median()           求中位数
df.var()              求方差
df.std()              求标准差
df.mad()              根据平均值计算平均绝对利差
df.cumsum()           求累计和
sr1.corr(sr2)         求相关系数
df.cov()              求协方差矩阵
df1.corrwith(df2)     求相关系数

pd.cut(array1, bins)  求一维数据的区间分布
pd.qcut(array1, 4)    按指定分位数进行区间划分，4可以替换成自定义的分位数列表   

df['col1'].groupby(df['col2']) 列1按照列2分组，即列2作为key
df.groupby('col1')    DataFrame按照列1分组
grouped.aggreagte(func) 分组后根据传入函数来聚合
grouped.aggregate([f1, f2,...]) 根据多个函数聚合，表现成多列，函数名为列名
grouped.aggregate([('f1_name', f1), ('f2_name', f2)]) 重命名聚合后的列名
grouped.aggregate({'col1':f1, 'col2':f2,...}) 对不同的列应用不同函数的聚合，函数也可以是多个


df.pivot_table(['col1', 'col2'], 
               rows=['row1', 'row2'], 
               aggfunc=[np.mean, np.sum]
               fill_value=0,
               margins=True)  根据row1, row2对col1， col2做分组聚合，聚合方法可以指定多种，并用指定值替换缺省值
               
          
pd.crosstab(df['col1'], df['col2']) 交叉表，计算分组的频率


```