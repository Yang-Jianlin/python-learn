import threading
import time


def task1(s):
    task_list = ['file1', 'file2', 'file3']
    for i in task_list:
        print('正在下载：{}'.format(i))
        time.sleep(s)
        print('下载成功：{}'.format(i))


def task2(s):
    task_list = ['music1', 'music2', 'music3', 'music4']
    for i in task_list:
        print('正在听音乐：{}'.format(i))
        time.sleep(s)


if __name__ == '__main__':
    t1 = threading.Thread(target=task1, args=(1,))  # 创建线程1
    t2 = threading.Thread(target=task2, args=(0.5,))  # 创建线程2
    t1.start()  # 启动线程
    t2.start()
