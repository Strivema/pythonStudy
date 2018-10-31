# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 下午4:35
# @Software: PyCharm
# import os
# print(os.uname())
import json
# d= dict(name='bob',age = 22,score=90)
# f = json.dumps(d)
# print(f)
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
s1 = json.dumps(obj,ensure_ascii=True)
print(s)
print(s1)