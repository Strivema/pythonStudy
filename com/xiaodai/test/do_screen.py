# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/16 上午10:42
# @Software: PyCharm
class Screen(object):
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width
    @height.setter
    def height(self,value):
        self._height = value
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def res(self):
        return self._height*self._width
s = Screen()
s.width=100
s.height = 1200
print(s.res)


