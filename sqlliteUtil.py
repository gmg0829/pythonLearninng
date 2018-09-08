import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor();
#创建表
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入数据
#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#查询
cursor.execute('select * from user where id=?', ('1',))
value=cursor.fetchall()
print(value)
cursor.rowcount
cursor.close()
conn.commit()
conn.close()
print("执行成功")