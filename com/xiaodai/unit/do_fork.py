# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 上午10:45
# @Software: PyCharm
import os
print(os.getpid())
pid = os.fork()
print(pid)
if pid ==0:
    print(os.getpid(),os.getppid())
else:
    print(os.getpid(),pid)