def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total = total + term
        count += 1
        average = total / count
        print(average)


a = averager()
next(a)
a.send(5)
a.send(10)
