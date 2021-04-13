import threading
import time


def thread_loop():
    print('Thread {0} is running'.format(threading.current_thread().name))
    for i in range(0, 5):
        print('thread {0} >>> {1}'.format(threading.current_thread().name, i))
        time.sleep(1)
    print('Thread {0} is ended'.format(threading.current_thread().name))


print('Thread {0} is running'.format(threading.current_thread().name))
t = threading.Thread(target=thread_loop, name='LoopThread')
t.start()
t.join()
print('Thread {0} is ended'.format(threading.current_thread().name))
