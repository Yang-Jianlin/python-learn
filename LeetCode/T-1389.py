class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(0, len(nums)):
            target.insert(index[i], nums[i])
        return target


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(s.createTargetArray(nums, index))
