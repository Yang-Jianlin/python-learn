class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0
        for i in range(1, x + 1):
            if i * i > x:
                return int(i - 1)

    def mySqrt2(self, x):
        start = 0
        end = x
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid - 1
            else:
                res = mid
                start = mid + 1
        return res


if __name__ == '__main__':
    s = Solution()
    x = 0
    print(s.mySqrt2(x))
