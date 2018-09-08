import xlwt
work=xlwt.Workbook(encoding='ascii')
worksheet=work.add_sheet('sheet',cell_overwrite_ok=True)
#初始化样式
style=xlwt.XFStyle()
#为样式创建字体
font=xlwt.Font()
#指定字体名字
font.name='Times New Roman'
#字体加粗
font.bold=True
#将该font设定为style的字体
style.font=font

worksheet.write(0,0,'姓名',style)
work.save('excel.xls')