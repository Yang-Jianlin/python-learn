"""
开发过程中使用线程，在线程间共享多个资源的时候，
如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不做任何事情。
"""
import threading
import time


lockA = threading.Lock()
lockB = threading.Lock()


def task1():
    if lockA.acquire(timeout=5):
        print('获取了A锁')  # 如果可以获取到锁则返回True
        time.sleep(0.5)
        if lockB.acquire(timeout=5):  # 如果锁被占用，等待
            print('又获取了B锁')
            lockB.release()
        lockA.release()


def task2():
    if lockB.acquire(timeout=5):
        print('获取了B锁')
        time.sleep(0.5)
        if lockA.acquire(timeout=5):
            print('又获取了A锁')
            lockA.release()
        lockB.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()
