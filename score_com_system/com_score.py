"""
用于成绩的计算，并返回{人名：成绩}字典：
成绩计算公式
必修课成绩=sum（各科成绩*学分）/总学分*0.7
选修课成绩=sum(各科成绩*学分)/总学分*0.3
最终成绩=必修课成绩+选修课成绩
"""


from score_com_system import stu_info
from score_com_system import wei_course


def comp_score():
    info = stu_info.nameInfo()
    req_course, ele_course, val_course = wei_course.weight()
    end_score = {}
    for i in info.keys():
        # 各类课的总成绩
        sum_score_req = 0
        sum_score_ele = 0
        sum_score_val = 0
        # 各类课的总学分
        count_req = 0
        count_ele = 0
        count_val = 0
        # 遍历字典，计算成绩
        for j in info[i].keys():
            if j in req_course:
                sum_score_req += float(info[i][j]['成绩']) * float(info[i][j]['学分'])
                count_req += float(info[i][j]['学分'])
            elif j in ele_course:
                sum_score_ele += float(info[i][j]['成绩']) * float(info[i][j]['学分'])
                count_ele += float(info[i][j]['学分'])
            else:
                sum_score_val += float(info[i][j]['成绩']) * float(info[i][j]['学分'])
                count_val += float(info[i][j]['学分'])
        if count_req == 16:  # 英语免修同学，英语按照95分计算
            sum_score_req += 190
            count_req += 2
        score = (float(sum_score_req / count_req * 0.7) + float(sum_score_ele / count_ele * 0.3)
                 + float(sum_score_val / count_val * 0))
        end_score[i] = score / 2
    return end_score
