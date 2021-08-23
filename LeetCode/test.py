# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         nums = list(set(nums))
#         nums.sort()
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    n = s.removeDuplicates(nums)
    print(n)
    print(nums)

