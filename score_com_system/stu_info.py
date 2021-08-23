"""
用于从文件中提取出每个学生的信息：
将信息以字典格式返回，
具体如
{
'Tom':{'math':{'score': '98', 'credit', '2'}, 'chinese':{'score': '90', 'credit', '3'}},
'Jhon':{'math':{'score': '92', 'credit', '2'}, 'chinese':{'score': '87', 'credit', '3'}},
}
"""

import re


def nameInfo():
    info = []  # 进行信息的存储，将文件的所有内容写入进列表中，作为转换字典的中间层
    flag = ''  # 进行人员变化标记
    per = []  # 将同一个人的各科信息记录写入同一个列表之中
    with open('score.txt', 'r', encoding='UTF-8') as info_file:  # 以可读方式打开文件，由于存在汉语，所以需要UTF-8格式
        while True:  # 每次读取文件的一行，文件中，每行就是一个人的一门课所有信息
            line = info_file.readline()
            if not line:  # 文件读取结束后，结束循环
                break
            line = line[:len(line) - 1]  # 将每行最后的换行符'\n'去掉
            line = re.split(r'[,; \t]', line)  # 将每行字符串格式的信息变成列表，例如:Tom math 98 2 --> ['Tom', 'math', '98', '2']

            # 利用flag进行人的标记，例如文件前五行为Tom的各科成绩记录，接下来四行为Jhon的各科成绩记录
            # 利用flag标记人的变化，方便将一个人的各科成绩记录写入一个列表中
            # 最终[[['Tom', 'math', '98', '2'], ['Tom', 'chinese', '90', '3']],
            # [['Jhon', 'math', '92', '2'], ['Jhon', 'chinese', '87', '3']]]
            if line[0] == flag:
                per.append(line)
            else:
                info.append(per)
                per = []  # 每次人变化之后，就将信息重新记录进per中
                flag = line[0]
                per.append(line)
        info.append(per)
    info = info[1:]  # 去除初始化per时的[]元素
    info_dict = {}
    # 对列表进行遍历，并转化为字典
    for i in info:
        new = {}
        for j in i:
            new[j[1]] = {'成绩': j[2], '学分': j[3]}
        info_dict[i[0][0]] = new
    return info_dict
