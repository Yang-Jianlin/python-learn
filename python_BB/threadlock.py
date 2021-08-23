import threading
import time
"""
两个线程共享一个全局变量，
每个线程都对变量进行操作，输出线程结束后的变量的值
"""
lock = threading.Lock()
tacket = 10000000


def task1():
    global tacket
    lock.acquire()
    for i in range(0, 1500000):
        tacket -= 1
    lock.release()


def task2():
    global tacket
    lock.acquire()
    for i in range(0, 1600000):
        tacket -= 1
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(tacket)
