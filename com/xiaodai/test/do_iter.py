for x in [1,2,3,4,5]:
    print(x)
    pass
it =iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break