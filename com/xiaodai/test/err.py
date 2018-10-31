# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 下午3:36
# @Software: PyCharm
from functools import reduce
import logging

def str2num(s):
    try:
       return int(s)
    except Exception as e:
        # logging.log(e)
        return float(s)
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    try:
        return reduce(lambda acc, x: acc + x, ns)
    except Exception as s:
        logging.exception(s)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
main()