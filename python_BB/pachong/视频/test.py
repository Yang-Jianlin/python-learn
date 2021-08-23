import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

# 使用线程池方式执行
start_time = time.time()


def get_page(*args):
    print("args0:{0}, args1:{1}".format(args[0], args[1]))
    time.sleep(2)
    print('下载成功：', args[0])


name_list = [('00', '0'), ('aa', 'a'), ('bb', 'b'), ('cc', 'c')]

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中每一个列表元素传递给get_page进行处理。
pool.map(get_page, name_list)
pool.close()
pool.join()
end_time = time.time()
print(end_time - start_time)
