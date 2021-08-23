class Solution:
    def longestPalindrome(self, s: str):
        s1 = s
        m = list(s)
        m.reverse()
        s2 = ''.join(m)
        len1 = len(s1)
        len2 = len(s2)

        array = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

        maxNum = 0  # 最长匹配长度
        p = 0  # 字符串匹配的终止下标

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    array[i][j] = array[i - 1][j - 1] + 1

                    if array[i][j] > maxNum:
                        beforeRev = len1 - 1 - j
                        if beforeRev + array[i][j] - 1 == i:
                            maxNum = array[i][j]
                            p = i - 1

        return s1[p + 1 - maxNum: p + 1]


if __name__ == '__main__':
    s = "aacabdkacaa"
    solu = Solution()
    print(solu.longestPalindrome(s))
