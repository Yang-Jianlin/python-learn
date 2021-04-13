def num():
    a = yield 1
    while True:
        a = yield a


c = num()
print(c.send(None))
print(c.send(5))
