from multiprocessing import Process
import time
import os


def task1(sec):
    while True:
        print('this is task1.', os.getpid(), os.getppid())
        time.sleep(sec)


def task2(sec):
    while True:
        print('this is task2', os.getpid(), os.getppid())
        time.sleep(sec)


if __name__ == '__main__':
    number = 1
    print(os.getpid())
    print('---------------')
    p1 = Process(target=task1, name='task01', args=(1, ))
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name='task02', args=(2, ))
    p2.start()
    print(p2.name)

    while True:
        if number == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print('number=', number)
            number += 1
            time.sleep(0.2)
