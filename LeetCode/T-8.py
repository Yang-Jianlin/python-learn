class Solution:
    def myAtoi(self, s: str):
        s = s.lstrip()
        if len(s) == 0:
            return 0
        elif len(s) == 1 and not s.isnumeric():
            return 0
        if not s[0].isnumeric() and s[0] != '-' and s[0] != '+':
            return 0
        elif not s[0].isnumeric() and not s[1].isnumeric():
            return 0
        else:
            num = ""
            flag = '+'
            if not s[0].isnumeric():
                flag = s[0]
                s = s[1:]
            for i in s:
                if i.isnumeric():
                    num += i
                else:
                    break
            num = flag + num
            num = int(num)
            if num > 2**31-1:
                num = 2**31-1
            elif num < -2**31:
                num = -2**31
            return num


if __name__ == '__main__':
    solu = Solution()
    s = "   +0 123"
    print(solu.myAtoi(s))

