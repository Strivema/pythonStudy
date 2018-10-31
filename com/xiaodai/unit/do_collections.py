# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 下午2:37
# @Software: PyCharm
from collections import Counter
c = Counter()
for ch in 'hello world':
    c[ch] = c[ch]+1
print(c)