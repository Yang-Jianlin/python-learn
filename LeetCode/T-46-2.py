class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums):
        num_digit = []
        for i in range(len(nums)):
            num_digit.append(nums)

        self.dfs([], 0, num_digit)
        return self.result

    def dfs(self, tmp, index, num_digit):
        if index == len(nums):
            self.result.append(tmp)
            return
        letters = num_digit[index]
        for i in letters:
            tmp.append(i)
            self.dfs(tmp, index + 1, num_digit)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.permute(nums))
