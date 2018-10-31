# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/18 7:04 PM
# @Software: PyCharm
import math
for i in range(1,10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x**2==i+100) and (y**2==i+268):
        print(i)