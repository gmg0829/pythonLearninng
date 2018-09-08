import urllib.request
import os
import re
from bs4 import BeautifulSoup
import shutil
import xlwt
def getName(soup_packtpage,name):
    all_book_title = soup_packtpage.find_all("div", class_="book-block-title")

    for book_title in all_book_title:
        c = book_title.string.strip()
        name.append(c)
    return name

def getPrice(soup_packtpage,price):
    all_book_price = soup_packtpage.find_all("div", class_="book-block-price-discounted ")
    all_book_prices = re.compile(u"\s+.\s+\d+.\d+")

    for book_price in all_book_price:
        book_prices = book_price.find_next(text=all_book_prices)
        d= book_prices.strip().replace(' ' ,'')
        price.append(d)

    return price

def save_excel(book_name,books_price):
    filename = xlwt.Workbook()
    sheet = filename.add_sheet("sheet1", cell_overwrite_ok=True)
    sheet.write(0,0,"book_title")                       #写入书名
    sheet.write(0,1,"book_price")                       #写入书价

    for i in range(len(book_name)):
        sheet.write(i+1,0,book_name[i])
        sheet.write(i+1,1,books_price[i])

    path = 'E:/'
    if os.path.isfile(path):          #判断路径是否为文件
        os.remove(path)               #删除指定路径的文件
    elif os.path.isdir(path):         #判断路径是否为目录
        shutil.rmtree(path, True)     #删除目录及目录内部的文件
    os.mkdir(path)                    #创建目录
    path = path + "packtpub.xls"
    first_col = sheet.col(0)          #设置宽度
    first_col.width = 256*70
    sec_col = sheet.col(1)
    sec_col.width = 256*10
    filename.save(path)
    print("创建excel文件完成!")


def main():
    all_html_name = []
    all_html_price = []
    for html in range(0,5064,12):
        url = "https://www.packtpub.com/all?search=&offset={0}&rows=&sort=".format(html)
        page = urllib.request.urlopen(url)
        soup_packtpage = BeautifulSoup(page,'html.parser')
        page.close()
        getName(soup_packtpage,all_html_name)          #获取书名
        getPrice(soup_packtpage,all_html_price)        #获取书价
        page_num = html / 12
        print("写入第{0}页".format(page_num+1))
    name = getName(soup_packtpage,all_html_name)
    price = getPrice(soup_packtpage,all_html_price)
    save_excel(name,price)                            #存入Excel

main()