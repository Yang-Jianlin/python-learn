from multiprocessing import Pool
import time
import os
import random


def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    time.sleep(random.random() * 2)
    end = time.time()
    print('完成任务:{}!用时:{},进程id:{}'.format(task_name, (end - start), os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)  # 进程池最多可以容纳5个进程
    task_name = ['听音乐', '吃饭', '洗衣服', '打游戏', '散步', '看孩子', '做饭']
    for i in task_name:
        pool.apply_async(task, args=(i, ))

    pool.close()  # 向主进程添加任务结束
    pool.join()  # 阻塞主进程，也就是说只有子进程结束主进程才能结束
    print('over!')

