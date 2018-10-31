# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 上午11:08
# @Software: PyCharm
import re
r =re.match(r'^\d{3}-\d{3,8}','010-12345')
s =re.match(r'^\d{3}-\d{3,8}','010 12345')
print(r)
print(s)
test='字符串'
if  re.match(r'字符串',test):
    print('ok')
else:
    print('fail')
print(r.group(0))