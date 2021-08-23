class Solution:
    def numWays(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            return self.numWays(n-1) + self.numWays(n-2)

    def numWays2(self, n):
        num = [1, 1, 2]
        for i in range(3, n+1):
            num.append(num[i-1]+num[i-2])
        return num[n]


if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.numWays(n))
