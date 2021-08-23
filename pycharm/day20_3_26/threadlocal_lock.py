import threading

local_ban = threading.local()


def deposit(num_money):
    balance = local_ban.money
    balance = balance + num_money
    balance = balance - num_money
    return balance


def thread_lop(balance, num):
    local_ban.money = balance
    a_num = 0
    for i in range(3):
        a_num = deposit(num)
    print(a_num)


t1 = threading.Thread(target=thread_lop, args=(15, 5))
t2 = threading.Thread(target=thread_lop, args=(0, 7))
t1.start()
t2.start()
t1.join()
t2.join()
