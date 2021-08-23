class Solution:
    def countPrimes(self, n: int):
        res = []
        for i in range(2, n):
            k = 2
            for j in range(2, i):
                k += 1
                if i % j == 0:
                    break
            if k >= i:
                res.append(i)
        return res


if __name__ == '__main__':
    n = 1000
    s = Solution()
    print(s.countPrimes(n))
