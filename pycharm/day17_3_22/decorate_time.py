import time
from functools import wraps


def decorate(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        dur_time = end - start
        print('the {0} execute time is {1}'.format(func.__name__, dur_time))
        # return func(*args, **kwargs)
    return wrapper


@decorate
def f1():
    print('start running f1()!')
    time.sleep(1)
    print('end running f1()!')


@decorate
def f2():
    print('start running f2()!')
    time.sleep(2)
    print('end running f2()!')


if __name__ == '__main__':
    f1()
    f2()
