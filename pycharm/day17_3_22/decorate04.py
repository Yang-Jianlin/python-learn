from datetime import datetime
import functools


def log(log_file='log.txt'):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("{0}'s log write the {1}".format(func.__name__, log_file))
            # str_info =
            with open(log_file, 'a') as log_info:
                log_info.write(func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@log('log.txt')
def now():
    time_now = datetime.now()
    print("now() was called time: {0}".format(time_now))


now()
print("called name is {0}".format(now.__name__))
