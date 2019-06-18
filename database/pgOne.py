#coding=utf-8

import psycopg2
import time


"""
一个进程处理一个表
"""
conn = psycopg2.connect(dbname="postgres", user="postgres",
        password="123456", host="192.168.1.166", port="5432")


io1 = open('user.csv', 'w')
sql1 = """copy (select * from "AML".user) to STDOUT delimiter ',' csv header"""


def table_size(table_name, c):
    cur = c.cursor()
    cur.execute("select pg_size_pretty(pg_relation_size('%s'));" % table_name)
    s = cur.fetchone()[0]
    cur.close()
    return s

print('user size:', table_size('"AML".user', conn))

s = time.time()
cur1 = conn.cursor()
cur1.copy_expert(sql1, io1)
cur1.close()


