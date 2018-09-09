from operator import itemgetter
list1=[123,10,45,-9]
#print(sorted(list1,reverse=True))
#print(sorted(list1,key=abs))
list2=['abc','Abd','Cd']
#忽略大小写
#print(sorted(list2,key=str.lower))
#反向排序
#print(sorted(list2,key=str.lower,reverse=True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=itemgetter(1),reverse=True))