# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 上午10:09
# @Software: PyCharm
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be int')
        if value<0 or value>100:
            raise ValueError('value must be 0-100')
        self._score = value

s = Student()
s.set_score(100)
print(s.get_score())
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('value must be int')
        if value < 0 or value > 100:
            raise ValueError('value must be 0-100')
        self._score = value
t = Student()
t.score=90
print(t.score)