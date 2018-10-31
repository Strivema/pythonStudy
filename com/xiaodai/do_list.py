L = [x**2 for x in range(1,11)if x%2==0]
print(L)
M = [m+n for m in 'ABC' for n in 'XYZ']
print(M)
import os
N=[d for d in os.listdir()]
print(N)
P = ['Hello', 'World', 18, 'Apple', None]
P_1 = [s.lower() for s in  P if isinstance(s,str)]
print(P_1)
g = (x**2 for x in range(1,11))
print(next(g))
print(g)