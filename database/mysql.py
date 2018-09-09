import pymysql
#打开数据库连接
def insert():
 db=pymysql.connect("localhost",'root','root','test')
 cursor=db.cursor()
 sql="insert into user(id,name) values(2,'yr')"
 try:
   cursor.execute(sql)
   db.commit()
 except:
    db.rollback()
    db.close()
#insert()
def findAll():
    db=pymysql.connect('localhost','root','root','test')
    cursor=db.cursor()
    sql="select * from user"
    cursor.execute(sql)
    result=cursor.fetchall()
    for user in result:
        id=user[0]
        name=user[1]
        print(id,name)
#findAll()
def findByid(id):
    db=pymysql.connect('localhost','root','root','test')
    cursor=db.cursor()
    sql="select * from user where id="+id
    cursor.execute(sql)
    result=cursor.fetchone()
    id=result[0]
    name=result[1]
    print(id,name)
#findByid('2')
def updqte(id):
    db = pymysql.connect('localhost', 'root', 'root', 'test')
    cursor = db.cursor()
    sql = "update user set name='gmgyr' where id=" + id
    cursor.execute(sql)
    db.commit()
    db.close()
#updqte('1')
def delete(id):
    db = pymysql.connect('localhost', 'root', 'root', 'test')
    cursor = db.cursor()
    sql = "delete from user where id=" + id
    cursor.execute(sql)
    db.commit()
    db.close()
delete('1')
