import os
import re
import datetime

file = open('data.txt', 'a')  # 以可写打开目标文件
for a in range(1, 10):
    ping = os.popen('ping www.baidu.com -n 1').read()  # 执行1次ping命令
    # ping = re.compile(r'来自..+', re.M).findall(ping)  # 通过正则表达式筛选出需要的哪一行
    nowTime = datetime.datetime.now()  # 获取当前系统的时间戳
    file.write(str(ping) + ' ,' + str(nowTime) + '\n')  # 写入内容
