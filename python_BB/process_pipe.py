from multiprocessing import Pipe, Process
import time
import random


def download1(p, args):
    for i in args:
        p.send(i)
        print('正在下载文件：{}'.format(i))
        time.sleep(random.random()*2)


def savefile(p):
    while True:
        file = p.recv()
        print('文件{}保存成功'.format(file))


if __name__ == '__main__':
    p = Pipe()
    args1 = ['url1', 'url3', 'url5', 'url7']
    down1 = Process(target=download1, args=(p[0], args1, ))
    save = Process(target=savefile, args=(p[1], ))
    down1.start()
    save.start()
    down1.join()
    save.terminate()
    print('over!')
