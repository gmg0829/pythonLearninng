import psycopg2
import time
import multiprocessing
# https://blog.csdn.net/weixin_43086579/article/details/84801384

conn1 = psycopg2.connect(dbname="postgres", user="postgres",
        password="123456", host="192.168.1.166", port="5432")
# conn2 = psycopg2.connect(dbname="postgres", user="postgres",
#         password="123456", host="192.168.1.166", port="5432")

io1 = open('user.csv', 'w')
io2 = open('userentity.csv', 'w')

sql1 = """copy (select * from "AML".user) to STDOUT delimiter ',' csv header"""
sql2 = """copy (select * from "AML".userentity) to STDOUT delimiter ',' csv header"""

def table_size(table_name, c):
    cur = c.cursor()
    cur.execute("select pg_size_pretty(pg_relation_size('%s'));" % table_name)
    s = cur.fetchone()[0]
    cur.close()
    return s

print('user size:', table_size('"AML".user', conn1))
print('userentity_size:', table_size('"AML".userentity', conn1))


def work(conn, sql, io):
    ss = time.time()
    cur = conn.cursor()
    cur.copy_expert(sql, io)
    print('PID {} cost: {}'.format(multiprocessing.current_process().pid, time.time() - ss))


multiprocessing.Process(target=work, args=(conn1, sql1, io1)).start()
multiprocessing.Process(target=work, args=(conn1, sql2, io2)).start()