# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 下午3:36
# @Software: PyCharm
import mysql.connector
conn = mysql.connector.connect(user='root',password='123456',database='test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()
cursor.close()