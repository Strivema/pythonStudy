# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/18 7:34 PM
# @Software: PyCharm
for i in range(1,10):
    for j in range(1,i+1):
        res = i*j
        print("%d*%d=%2d" % (j,i,i*j),end=' ')
    print(' ')