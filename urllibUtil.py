from urllib import  request
with request.urlopen('https://github.com/') as f:
    data=f.read()
    #获取状态码
    #print('status',f.status,f.reason)
    #获取header
    '''
       for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    '''
    print('data:',data.decode('utf-8'))