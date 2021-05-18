"""
可以用递归的方法来解决问题。
1）我们先确定字符串第一个字母是谁，对于长度为n的字符串，总共有n种情况；
2）然后呢，问题就从“返回字符串中的字母排列组合” 变成了 “返回 第一个字母+除去第一个字母外的字符串的排列组合”，有点大而化小，分而治之的感觉。
"""


def perm(s):
    # 这里是递归函数的出口，为什么呢，因为这里表示：一个长度为1的字符串，它的排列组合就是它自己。
    if len(s) <= 1:
        return [s]
    sl = []  # 保存字符串的所有可能排列组合
    for i in range(len(s)):  # 这个循环，对应 解题思路1）确定字符串的第一个字母是谁，有n种可能（n为字符串s的长度
        for j in perm(s[0:i] + s[i + 1:]):  # 这个循环，对应 解题思路2）进入递归，s[0:i]+s[i+1:]的意思就是把s中的s[i]给去掉
            sl.append(s[i] + j)  # 对应 解题思路2）问题就从“返回字符串中的字母排列组合” **变成了** “返回 第一个字母+除去第一个字母外的字符串的排列组合”
    return sl


def main():
    perm_nums = perm('catdog')  # 有可能存在字母相同的情况
    no_repeat_nums = list(set(perm_nums))  # 利用集合中没有重复的元素
    print('perm_nums', len(perm_nums), perm_nums)
    print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
    pass


if __name__ == '__main__':
    main()
