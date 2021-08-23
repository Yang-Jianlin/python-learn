"""
用于将文件中的记录的课程提取出来：
并且分为3类，选修，必修以及不计入成绩的课
"""


import re


def weight():
    flag_choose = ['知识发现与数据挖掘', '英语科技论文写作', '专业写作', '高级JAVA语言程序设计',  '习近平谈治国理政']  # 选修课
    flag_invalid = ['机器学习', '创新创业活动']  # 不计入成绩课
    # 利用集合防止重复课程计入
    req_course = set()
    ele_course = set()
    val_course = set()
    with open('score.txt', 'r', encoding='UTF-8') as info_file:
        while True:
            line = info_file.readline()
            if not line:
                break
            line = line[:len(line)-1]
            line = re.split(r'[,; \t]', line)
            if line[1] in flag_choose:
                ele_course.add(line[1])
            elif line[1] in flag_invalid:
                val_course.add(line[1])
            else:
                req_course.add(line[1])
    req_course = list(req_course)
    ele_course = list(ele_course)
    val_course = list(val_course)
    return req_course, ele_course, val_course
