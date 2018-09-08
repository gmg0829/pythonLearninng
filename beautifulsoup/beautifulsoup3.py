import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import shutil

def get_qb(page_num):
    list_qs = []
    url = 'https://www.qiushibaike.com/hot'
    for page in range(1, page_num + 1):
        cnt = 0
        qbhot = '{0}/page/{1}'.format(url, str(page))
        print("开始获取第{0}页糗事...".format(page))
        r = requests.get(qbhot)
        soup = BeautifulSoup(r.text, "lxml")
        for tag in soup.find_all("div",attrs = {"class":'content'}):
            if tag.contents[1].string != None:
                content = tag.contents[1].string.strip()
                list_qs.append(content)
                cnt += 1

        print('{0}条'.format(cnt))
        if page % 4 is 0:
            sleep(1)
    return list_qs

def main():
    page_num = 13
    file_qb = "F:\\"
    if os.path.isfile(file_qb):
        os.remove(file_qb)
    if os.path.isdir(file_qb):
        shutil.rmtree(file_qb,True)
    os.mkdir(file_qb)
    file_qb = file_qb +"qiubai.txt"
    ls_qs = get_qb(page_num)
    with open(file_qb, 'w', encoding='utf-8') as f:
        f.write('\n'.join(ls_qs))

    print("完成!")

main()