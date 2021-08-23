class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0, 1, 2]
        for i in range(3, n+1):
            count.append(count[i-1] + count[i-2])
        return count[n]


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.climbStairs(n))
