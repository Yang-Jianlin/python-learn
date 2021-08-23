from python_BB.pachong.药监局 import getID, getInfo
import time

if __name__ == '__main__':
    start = time.time()
    getID.get_id()
    getInfo.get_info()
    end = time.time()
    spend_time = end - start
    print('执行完毕！耗时{}秒！'.format(spend_time))
