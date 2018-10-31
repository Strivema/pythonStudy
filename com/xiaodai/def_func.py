import math
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad type')
    if x>=0:
        return x
    else:
        return -x

# print(my_abs(-100))
def add_end(L=[]):
    L.append('End')
    return L

# print(add_end())
# print(add_end())
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
print(add_end())
# print(add_end())
def calc(num):
    sum = 0
    for n in num:
        sum = sum+n**2
    return sum
print(calc([1,2,3,4]))

def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n ** 2
    return sum
print(calc(1,2))
