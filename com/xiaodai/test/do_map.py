from functools import reduce
def normalize(name):
    return name[:1].upper()+name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
print(prod([3,5,7,9]))