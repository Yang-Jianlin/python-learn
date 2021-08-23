class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = 0
        if x < 0:
            x = str(x)[1:]
            x = x[::-1]
            x = '-' + x
            res = int(x)
        elif x > 0:
            x = str(x)
            x = x[::-1]
            res = int(x)
        if res > 2**31-1 or res <-2**31:
            res = 0
        return res


if __name__ == '__main__':
    s = Solution()
    x = -120
    print(s.reverse(x))
