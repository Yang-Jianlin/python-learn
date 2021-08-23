def simple_coro(a):
    print('-> start: a = ', a)
    b = yield a
    print('-> receive: b = ', b)
    c = yield a + b
    print('-> receive: c = ', c)


simple_coro(3)
next(s)
s.send(6)
s.send(12)
