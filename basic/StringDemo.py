import re
str1='hello'
str2='world'
str=str1+str2
#print(str)
str3=['hi','hello','python']
#print('.'.join(str3))
phone='137-1111-1126'
#print(phone.split('-'))
#print(phone.find('6'))
line='-ssss-'
#print(line.strip('-'))
patt=re.compile(r'^(137|184)\d{6,8}$')
strr='137456781'
m=re.match(patt,strr)
if m:
    print('match')
else:
    print('no match')