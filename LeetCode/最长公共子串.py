def getMaxCommonSubstr(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    array = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

    maxNum = 0  # 最长匹配长度
    p = 0  # 字符串匹配的终止下标

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if text1[i-1] == text2[j-1]:
                array[i][j] = array[i-1][j-1] + 1

                if array[i][j] > maxNum:
                    maxNum = array[i][j]
                    p = i - 1

    return maxNum, text1[p + 1 - maxNum: p + 1]


if __name__ == "__main__":
    s1 = 'abcdef'
    s2 = 'bcxdef'
    [lenMatch, strMatch] = getMaxCommonSubstr(s1, s2)
    print('子串: ', strMatch)
    print('子串长度: ', lenMatch)
