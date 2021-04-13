from functools import wraps


def log_info(logfile='log_s.txt'):
    print('log_info was called!')

    def log_decorate(func):
        @wraps(func)
        def function(*args, **kwargs):
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(logfile, 'r') as file_info:
                file_info.write(log_string)
            return func(*args, **kwargs)
        return function()
    return log_decorate


@log_info('log.txt')
def function():
    pass


function()
