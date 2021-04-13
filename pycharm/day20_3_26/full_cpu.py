import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    print("time:{0}".format(start))
    x = 0
    while True:
        x = x ^ 1


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(10)
    for i in range(11):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')