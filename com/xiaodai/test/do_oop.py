# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/15 下午5:21
# @Software: PyCharm
class Animal(object):
    def run(self):
        print('Animal is running')
class Dog(Animal):
    def run(self):
        print('Dog is running')
    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    pass
dog = Dog()
cat =Cat()
print(dog.run(),cat.run(),dog.eat())
print(len('abc'))
print('abc'.__len__())
class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count +=1
def main():
    san = Student('zhangsan')
    num = Student.count
    print(num)
    si = Student('lisi')
    num = Student.count
    print(num)
main()



