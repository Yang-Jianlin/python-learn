class Solution:
    def search(self, nums, target: int) -> int:
        return self.half_search(nums, 0, len(nums) - 1, target)

    def half_search(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid

        return self.half_search(nums, low, high, target)


if __name__ == '__main__':
    s = Solution()
    nums = []
    target = 2
    print(s.search(nums, target))
