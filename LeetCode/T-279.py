from math import sqrt

class Solution:
    def numSquares(self, n: int, count):
        num = sqrt(n)
        if int(num) == num:
            return count
        for i in range(1, n+1):
            if i*i >= n:
                j = i-1
                count += 1
                n = n-j*j
                break
        return self.numSquares(n, count)


if __name__ == '__main__':
    s = Solution()
    n = 12
    count = 1
    print(s.numSquares(n, count))
