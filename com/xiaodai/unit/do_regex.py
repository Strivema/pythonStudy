# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 上午11:20
# @Software: PyCharm
import re
def test(addr):
    if re.match(r'(^\w+)@(\w+).(com$)',addr):
        return True
    else:
        return False
print(test('a111@sin.com'))
