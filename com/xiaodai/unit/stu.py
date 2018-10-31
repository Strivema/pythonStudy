# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 下午4:05
# @Software: PyCharm
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
