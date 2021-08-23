class Solution:
    # 递归
    def fib1(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib1(n-1) + self.fib1(n-2)

    # 数组
    def fib2(self, n):
        a = 0
        b = 1
        c = a + b
        if n == 0:
            return a
        if n == 1:
            return b
        for i in range(2, n+1):
            c = a+b
            a = b
            b = c
        return c


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.fib1(n))
    print(s.fib2(n))
