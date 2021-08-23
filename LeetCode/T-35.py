class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [5, 7, 7, 7, 8, 8, 8, 8, 10]
    target = 8
    s = Solution()
    print(s.searchInsert(nums, target))
