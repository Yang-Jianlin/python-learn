class Solution:
    def __init__(self):
        self.res = []
        self.temp = []

    def permute(self, nums):
        n = 1
        for i in range(1, len(nums) + 1):
            n *= i
        self.dfs(nums, 0, n)
        return self.res

    def dfs(self, nums, position, n):
        if position == len(nums):
            self.res.append(self.temp[:])
            return
        else:
            for i in nums:
                if i not in self.temp:
                    self.temp.append(i)
                    self.dfs(nums, position + 1, n)
                    self.temp.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
