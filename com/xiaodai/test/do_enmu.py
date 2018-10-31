# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 上午11:39
# @Software: PyCharm
from enum import Enum,unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1
class Stuedent(object):
    def _init_(self,name,gender):
        self._name = name
        self._gender = gender
s= Stuedent('java',Gender.Male)
s.gender = Gender.Male
print(s.name,s.gender)

