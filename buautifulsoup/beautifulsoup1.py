import urllib.request
import datetime
import re
from bs4 import BeautifulSoup
starttime = datetime.datetime.now()

url = "https://www.packtpub.com/all"
page = urllib.request.urlopen(url)
soup_packtpage = BeautifulSoup(page,'html.parser')
page.close()

endtime  = datetime.datetime.now()
print(endtime - starttime)

starttime = datetime.datetime.now()

all_book_title = soup_packtpage.find_all("div", class_="book-block-title")
all_book_price = soup_packtpage.find_all("div", class_="book-block-price-discounted ")
a = []
b = []
all_book_prices = re.compile(u"\s+.\s+\d+.\d+")
for book_title in all_book_title:
    c = book_title.string.strip()
    a.append(c)

for book_price in all_book_price:
    book_prices = book_price.find_next(text=all_book_prices)
    d= book_prices.strip().replace(' ' ,'')
    b.append(d)
for book in range(len(a)):
    print("The price of " '《' '{0}' '》' " is "  '{1}' .format(a[book],b[book]))




endtime = datetime.datetime.now()

print(endtime - starttime)