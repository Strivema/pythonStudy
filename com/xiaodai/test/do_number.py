def is_ok(n):
    num = str(n)
    return num ==num[::-1]
print(list(filter(is_ok,range(1,1000))))