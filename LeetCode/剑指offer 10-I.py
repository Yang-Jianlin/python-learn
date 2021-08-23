class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            a, b = 0, 1
            i = 0
            while i <= n:
                yield a -
                a, b = b, a+b
                i += 1
        r = fun(n)
        result = []
        while True:
            try:
                result.append(next(r))
            except:
                break
        return result[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.fib(5))
