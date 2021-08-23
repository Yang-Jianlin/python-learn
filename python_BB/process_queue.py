"""
利用多进程模拟下载文件程序：
开启两个进程进行文件下载，然后再开启一个进程保存下载的文件
"""


from multiprocessing import Queue, Process
import time
import random


def download1(q, args):
    for i in args:
        q.put(i)
        print('正在下载文件：{}'.format(i))
        time.sleep(random.random()*2)


def download2(q, args):
    for i in args:
        q.put(i)
        print('正在下载文件：{}'.format(i))
        time.sleep(random.random()*2)


def savefile(q):
    while True:
        file = q.get()
        print('文件{}保存成功'.format(file))


if __name__ == '__main__':
    q = Queue(5)  # 队列中可以保存的元素上限，只有元素取出后，才会有下一个进入
    args1 = ['url1', 'url3', 'url5', 'url7']
    args2 = ['url2', 'url4', 'url6']
    down1 = Process(target=download1, args=(q, args1, ))
    down2 = Process(target=download2, args=(q, args2, ))
    save = Process(target=savefile, args=(q, ))
    down1.start()
    down2.start()
    save.start()
    down1.join()
    down2.join()
    save.terminate()
    print('over!')
