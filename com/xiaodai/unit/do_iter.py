# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 下午2:55
# @Software: PyCharm
import itertools
for c in itertools.chain('ABC','XYZ'):
    print(c)
for key,group in itertools.groupby('ababaaaaddnnnaddaqqqqq'):
    print(key,list(group))