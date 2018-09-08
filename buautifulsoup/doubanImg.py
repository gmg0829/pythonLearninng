import urllib.request,os,sys,re

if __name__ == '__main__':
   print('程序自身在运行');
else:
   print('我来自另一模块');

# 下载进度
def process(a,b,c):
    # a: 已经下载的数据块
    # b:数据块的大小
    # c:远程文件的大小
    per = 100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%'%per)

filepath = "F:\\img"
def savefile(path):
    if not os.path.isdir(filepath):
        os.mkdir(filepath)
    pos = path.rindex('/')
    t = os.path.join(filepath,path[pos+1:])
    return t
url =  "http://www.douban.com";
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'};
request = urllib.request.Request(url = url,headers = headers);
response = urllib.request.urlopen(request);
data = response.read();
data = data.decode("utf-8");
# print(data);
print(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data)))
for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link+'---'+t)
    try:
        urllib.request.urlretrieve(link,savefile(link),process)   #下载到本地
    except:
        print(link+"下载失败")

print(type(response));
print(response.geturl());
print(response.info());
print(response.getcode());