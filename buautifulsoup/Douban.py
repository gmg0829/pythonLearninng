from urllib import request
def savepath(data):
    path="F:\\douban.out"
    f=open(path,'wb')
    f.write(data)
    f.close()
url='https://m.douban.com/'
headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}
req=request.Request(url=url,headers=headers)
response = request.urlopen(req)
data = response.read()
savepath(data)

data=data.decode('utf-8')
code=response.getcode()
info=response.info()

print(data)
print(code)
print(info)
print(type(response))
print(response.geturl())
