import threading
import time

balance = 0


def deposit(num_money):
    global balance
    balance = balance + num_money
    balance = balance - num_money


def thread_lop(num):
    print('Thread {0} start time is {1}'.format(
        threading.current_thread().name, time.strftime('%H:%M:%S')))
    for i in range(3000000):
        deposit(num)
    print('Thread {0} end time is {1}'.format(
        threading.current_thread().name, time.strftime('%H:%M:%S')))


if __name__ == '__main__':
    print('Thread {0} start time is {1}'.format(
        threading.current_thread().name, time.strftime('%H:%M:%S')))
    t1 = threading.Thread(target=thread_lop, args=(5,))
    t2 = threading.Thread(target=thread_lop, args=(7,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Thread {0} end time is {1}'.format(
        threading.current_thread().name, time.strftime('%H:%M:%S')))

    print(balance)
