from collections import Iterable
a=isinstance([],Iterable)
b = isinstance({},Iterable)
c = isinstance('abc',Iterable)
d = isinstance((x for x in range(10)),Iterable)
e = isinstance(100,Iterable)
print(a,b,c,d,e)
