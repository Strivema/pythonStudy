import functools
int = functools.partial(int,base=2)
print(int('1000'))