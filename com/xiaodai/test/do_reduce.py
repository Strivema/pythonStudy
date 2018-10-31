from functools import reduce
def sum(x,y):
    return x+y
a = reduce(sum,[1,2,3,4,5])
print(a)
def str_float(s):
    s = s.split('.')
    def fn(x,y):
        return x*10+y
    def dn(x,y):
        return x/10+y
    def str2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(str2num,s[0]))+reduce(dn,map(str2num,s[1][::-1]))/10
print(str_float('123.456'))