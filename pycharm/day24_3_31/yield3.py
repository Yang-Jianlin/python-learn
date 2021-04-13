from coroutil import coroutine


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        try:
            total = total + term
            count += 1
            average = total / count
        except Exception as info:
            print(info)
        finally:
            print(average)


a = averager()
a.send(5)
a.send(10)
a.send('dfs')
