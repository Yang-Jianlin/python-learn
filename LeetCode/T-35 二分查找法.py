# 34\35\69

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid


if __name__ == '__main__':
    nums = [1, 5, 7, 9, 11]
    target = 8
    s = Solution()
    print(s.searchInsert(nums, target))
