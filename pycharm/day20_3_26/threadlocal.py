import threading

local_stu = threading.local()


def process_stu():
    std = local_stu.student
    print('Hello, {0} ({1})'.format(std, threading.current_thread().name))


def process_thread(name):
    local_stu.student = name
    process_stu()


t1 = threading.Thread(target=process_thread, args=('Alice',))
t2 = threading.Thread(target=process_thread, args=('Tom',))
t1.start()
t2.start()
t1.join()
t2.join()
