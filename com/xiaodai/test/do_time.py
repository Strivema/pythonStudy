# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/29 10:25 PM
# @Software: PyCharm
import time
def do_time():
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.gmtime(time.time()))
def do_test():
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
    print(end-start)
def do_clock():
    start = time.clock()
    for i in range(200):
        print(i)
    end = time.clock()
    print(end-start)
do_clock()