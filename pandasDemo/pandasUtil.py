import pandas as pd
fileNameStr='hospitalData.xlsx'          #读取Ecxcel数据
xls = pd.ExcelFile(fileNameStr, dtype='object')
salesDf = xls.parse('Sheet1',dtype='object')
#print(salesDf.head())#前五行
#print(salesDf.shape)#多少行，多少列
#print(salesDf.dtypes)#查看每列的数据类型
#选取子集
#print(salesDf.loc[0:4,'购药时间':'销售数量'])
#列名重命名
colNameDict = {'购药时间':'销售时间'}                  #将‘购药时间’改为‘销售时间’
salesDf.rename(columns = colNameDict,inplace=True)
#print(salesDf.head())                                 #查看前五行
print('删除缺失值前大小',salesDf.shape)
# how='any'意为在给定的任何一列中有缺失值就删除
salesDf=salesDf.dropna(subset=['销售时间','社保卡号'],how='any') #删除列（销售时间，社保卡号）中为空的行
print('删除缺失后大小',salesDf.shape)
#数据类型转换
salesDf['销售数量'] = salesDf['销售数量'].astype('float')
salesDf['应收金额'] = salesDf['应收金额'].astype('float')
salesDf['实收金额'] = salesDf['实收金额'].astype('float')
#print('转换后的数据类型：\n',salesDf.dtypes)

#修改时间格式
def splitSaletime(timeColSer):
    timeList = []
    for value in timeColSer:  # 例如2018-01-01 星期五，分割后为：2018-01-01
        dateStr = value.split(' ')[0]
        timeList.append(dateStr)

    timeSer = pd.Series(timeList)  # 将列表转行为一维数据Series类型
    return timeSer
timeSer=salesDf.loc[:,'销售时间']    #获取“销售时间”这一列
dateSer=splitSaletime(timeSer)      #对字符串进行分割，获取销售日期
salesDf.loc[:,'销售时间']=dateSer    #修改销售时间这一列的值
#print(salesDf.head())
#字符串转日期
salesDf.loc[:,'销售时间']=pd.to_datetime(salesDf.loc[:,'销售时间'],
                                    format='%Y-%m-%d',
                                    errors='coerce')
salesDf=salesDf.dropna(subset=['销售时间','社保卡号'],how='any')
#print(salesDf.dtypes)

#数据排序
print('排序前的数据集')
#print(salesDf.head())
salesDf=salesDf.sort_values(by='销售时间',     #按销售日期进行升序排列
                    ascending=True)
print('排序后的数据集')
#重命名行号
salesDf=salesDf.reset_index(drop=True)
#print(salesDf.head(3))
#异常值处理
#数据框中所有数据每列的描述统计信息
# count：总数，mean：平均数，std：标准差，min：最小值，25%：下四分位数，50%：中位数，75%：上四分位数，max：最大值
print(salesDf.describe())
