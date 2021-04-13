from pymemcache.client.base import Client
import time
import timeit
import random


# 计算平方的函数，若缓存中有就直接返回缓存的数据，若没有就重新计算，并写入缓存中
def compute_square(mc, num):
    value = mc.get('sq:%d' % num)
    if value is None:
        time.sleep(0.02)
        value = num * num
        mc.set('sq:%d' % num, value)
    return value


def mem_cache():
    mc = Client(('127.0.0.1', 11211))

    def make_request():
        compute_square(mc, random.randint(0, 15))

    print('Ten successive runs:')
    for i in range(1, 11):
        print('%.2fs' % timeit.timeit(make_request, number=10), end=' ')
    print()


if __name__ == '__main__':
    mem_cache()
