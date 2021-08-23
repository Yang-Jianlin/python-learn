class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        nums = [0] * n
        nums[0] = 1
        for i in range(1, n):
            nums[i] = min(2*nums[p2], 3*nums[p3], 5*nums[p5])
            if nums[i] == 2*nums[p2]:
                p2 += 1
            if nums[i] == 3*nums[p3]:
                p3 += 1
            if nums[i] == 5*nums[p5]:
                p5 += 1
        return nums[n-1]


if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.nthUglyNumber(n))
