class Solution:
    def searchRange(self, nums, target):

        def bisect_left(num):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if num <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        begin = bisect_left(target)
        if begin == len(nums) or nums[begin] != target:
            return [-1, -1]
        return [begin, bisect_left(target + 1) - 1]


if __name__ == '__main__':
    nums = [5, 7, 7, 7, 8, 8, 8, 10]
    target = 8
    s = Solution()
    print(s.searchRange(nums, target))
