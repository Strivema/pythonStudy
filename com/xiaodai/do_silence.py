# L = ['Michael', 'Sarah', 'Tracy', 'Bob','Jack','Marie']
# print(L[0],L[1])
# print(L[:3])
# print(L[1:3])
# print(L[-2:])
L= list(range(100))
print(L[:10:3])
print(L[::5])
print()
def trim(s):
    s = str.strip(s,' ')
    return s
