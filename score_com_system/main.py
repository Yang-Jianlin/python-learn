"""
main函数：
将成绩字典转为列表，并逆序输出(成绩从高到低)
并将成绩记录写入result文件中
"""


import time
from score_com_system import com_score


if __name__ == '__main__':
    start = time.time()
    # 每次运行系统将result文件清空，防止新的结果在上一轮结果后追加
    with open('result.txt', 'w', encoding='UTF-8') as res_file:
        res_file.write('')
    result = com_score.comp_score()
    res = []
    for i in result.keys():
        res.append([i, result[i]])
    # 按照成绩逆序排序
    res = sorted(res, key=lambda k: k[1], reverse=True)
    print(res)
    for i in res:
        with open('result.txt', 'a', encoding='UTF-8') as res_file:
            r = i[0] + ':' + str(round(i[1], 3)) + '\n'
            res_file.write(r)
    end = time.time()
    print('计算完毕，用时{0}秒！'.format(end-start))
