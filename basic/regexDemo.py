import re
#正则表达式
patt=re.compile(r'^(137|184)\d{6,8}$')
strr='137456781'
m=re.match(patt,strr)
if m:
    print('match')
else:
    print('no match')