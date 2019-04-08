#初始化
#info = {"name" : 'cold'}
info = dict(name = 'cold',age=12)
#获取
print(info['name'],info.get('age'))
#更新和添加
info['address']='sx'
#info.update(address='bj')
info.update(name='summer')
print(info)
#删除
info.pop('name')
print(info)
#获取所有key
print(info.keys())
print(info.values())
print(info.items())
info.clear();
