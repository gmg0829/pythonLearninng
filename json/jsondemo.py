import json
data={'a':'gmg','b':2}
#js=json.dumps(data) # json对象转为字符串
json.load('["foo", {"bar":["baz", null, 1.0, 2]}]'); #字符串转为json对象
print(data["a"])
