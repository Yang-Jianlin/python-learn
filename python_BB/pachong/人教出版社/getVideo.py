"""
https://www.imeijutv.com/play/40721-1-0.html
"""

import requests
import time
import os
import shutil  # os.mkdir('要清空的文件夹名')
import threading
from multiprocessing.dummy import Pool
time_start = time.time()


# 获取视频流切片的对应网址，下载视频切片就按照文件内的网址进行下载
def get_m3u8():
    url = "http://chuangcache.gensee.com/gsgetrecord/record50.gensee.net/gsrecord/183681/upload/2021_07_13/67533211_1626144023/hls/record1.m3u8"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    response_data = requests.get(url=url, headers=headers).text
    with open('data.txt', 'w', encoding='utf-8') as fp:
        fp.write(response_data)
    print('链接获取完成！')


# 对文件的视频流地址进行提取并划分为8个文件，方便启用八线程下载
def spl_file():
    if not os.path.exists('filedir'):
        os.mkdir('filedir')

    with open('data.txt', 'r', encoding='utf-8') as fp:
        flag, num = 0, 1
        while True:
            link = fp.readline()
            if not link:
                break
            filename = 'filedir/' + 'thread' + str(num)
            with open(filename, 'a') as fp1:
                fp1.write(link)
            flag += 1
            if flag == 256:
                flag = 0
                num += 1


# 根据获取的视频切片链接下载视频切片
def get_video(*args):
    filename, num = args[0], args[1]
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }

    if not os.path.exists('videoTS'):
        os.mkdir('videoTS')

    with open(filename, 'r', encoding='utf-8') as fp:
        pre_url = 'http://chuangcache.gensee.com/gsgetrecord/record50.gensee.net/gsrecord/183681/upload/2021_07_13/67533211_1626144023/hls/'
        flag = 0
        while True:
            link = fp.readline()
            if not link:
                break
            if link[:5] == "start":  # 提取出下载链接的行
                re_link = pre_url + link[:len(link) - 1]  # 去掉换行符
                tmp = str(time.time()).split('.', 2)  # 以下载时间对视频片段进行排序
                # 为了保证视频切片有序，需要依照每个线程的进行变换，如线程1，编号1+下载时间.ts，线程2，编号2+下载时间.ts
                tsName = 'videoTS/' + str(num) + '-' + ''.join(tmp) + '.ts'
                fp_video = open(tsName, 'wb')
                response_video = requests.get(url=re_link, headers=headers).content
                fp_video.write(response_video)
                fp_video.close()
                print('线程{0}------{1}------'.format(num, flag))
                time_end = time.time()
                print('已用时：', time_end - time_start, 's')
                flag += 1
    print('线程{0}下载完成'.format(num))


if __name__ == '__main__':
    # 开始时对下载路径存储的文件夹进行清空
    try:
        shutil.rmtree('filedir')
        shutil.rmtree('videoTS')
    except Exception as error:
        print('pass')
    time.sleep(0.1)

    get_m3u8()
    spl_file()
    time.sleep(0.1)

    t1 = threading.Thread(target=get_video, args=('filedir/thread1', 1,))
    t2 = threading.Thread(target=get_video, args=('filedir/thread2', 2,))
    t3 = threading.Thread(target=get_video, args=('filedir/thread3', 3,))
    t4 = threading.Thread(target=get_video, args=('filedir/thread4', 4,))
    t5 = threading.Thread(target=get_video, args=('filedir/thread5', 5,))
    t6 = threading.Thread(target=get_video, args=('filedir/thread6', 6,))
    t7 = threading.Thread(target=get_video, args=('filedir/thread7', 7,))
    t8 = threading.Thread(target=get_video, args=('filedir/thread8', 8,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    # pool = Pool(8)
    # param = []
    # for i in range(1, 9):
    #     a = ('filedir/thread'+str(i), i, )
    #     param.append(a)
    #
    # pool.map(get_video, param)
    # pool.close()
    # pool.join()
