"""
使用多进程导入multiprocessing中的Process；
模拟两个任务的执行，每次任务执行有暂停时间，并输出进程的ID和父ID
"""


from multiprocessing import Process
import time
import os


def task1(*args):
    while True:
        print("执行{}, ID:{}, PPID：{}".format(args[0], os.getpid(), os.getppid()))
        time.sleep(args[1])  # 睡眠时间


def task2(*args):
    while True:
        print("执行{}, ID:{}, PPID：{}".format(args[0], os.getpid(), os.getppid()))
        time.sleep(args[1])


if __name__ == '__main__':
    print('父进程ID：', os.getpid())  # 两个子进程创建之前，先打印出父进程ID
    print('------------------------')
    t1 = Process(target=task1, args=('任务一', 1))  # 子进程1执行任务一
    t2 = Process(target=task2, args=('任务二', 2))  # 子进程2执行任务二
    t1.start()  # start()方法来生成进程
    t2.start()
