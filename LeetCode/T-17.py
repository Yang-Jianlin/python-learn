"""
电话号码，实质上就是全排列
[1, 2, 3]全排列实际上就是[[1, 2, 3], [1, 2, 3], [1, 2, 3]]组合，去掉重复的
电话键盘“234”的组合实际上就是[[a, b, c], [d, e, f], [g, h, i]]的组合
所以全排列就多一句：if i not in self.temp:
"""


class Solution:
    def __init__(self):
        self.result = []
        self.tmp = []

    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        num_digit = []
        res = []
        flag, num = 3, 2
        for y in range(ord('a'), ord('z') + 1):
            res.append(chr(y))
            if len(res) == flag:
                num_digit.append(res)
                res = []
                num += 1
            if num == 7 or num == 9:
                flag = 4
            else:
                flag = 3

        self.dfs(0, digits, num_digit)
        return self.result

    def dfs(self, index, digits, num_digit):
        if index == len(digits):
            self.result.append(''.join(self.tmp[:]))
            return
        c = digits[index]
        letters = num_digit[int(c) - 2]
        for i in letters:
            self.tmp.append(i)
            self.dfs(index + 1, digits, num_digit)
            self.tmp.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('234'))
