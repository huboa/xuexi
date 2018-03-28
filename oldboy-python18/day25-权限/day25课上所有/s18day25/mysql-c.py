#!/usr/bin/python3

import pymysql
import mysql.connector

# conn  = mysql.connector.connect(user='test', password='!QAZ2wsx', database='mysql', use_unicode=True)
# cursor = conn.cursor()
# # cursor('show tables;')
conn = pymysql.connect("192.168.86.130",'test','!QAZ2wsx',charset='utf8')
cursor = conn.cursor()
sql = "select user,host from mysql.user;"
cursor.execute(sql) ###总数
# res=cursor.execute(sql) ###总数
rows=cursor.fetchall()   ###查询到的内容
for n in rows:
    print(n[1],type(n)) ## 打印内容

cursor.close()  #关闭数据
conn.close()##关闭连接