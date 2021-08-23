class Solution(object):
    def search(self, nums, target):
        for i in range(0, len(nums)):
            if target == nums[i]:
                return i
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(s.search(nums, target))
