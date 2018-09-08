import xlrd
data=xlrd.open_workbook('hello.xlsx') #获取excel
table=data.sheets()[0] #获取一个工作表
#data.sheet_by_index(0) 通过索引
#data.sheet_by_name('sheet1')#通过名字
# print(table.row_values(0)) #获取整行的值
# print(table.col_values(0))#获取整列的值
#print(table.nrows) #获取行数
#print(table.ncols) #获取列数
#print(table.cell(0,0).value)
#print(data.sheet_names());#获取所有薄的名字

#将table中第一行的数据读取并添加到data_list中，打印出第一行的全部数据
data_list=[]
data_list.extend(table.row_values(0))
for item in data_list:
    print(item)
#获取每行的值
for rownum in range(table.nrows):
    print(table.row_values(rownum))

