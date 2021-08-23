class Solution:
    def majorityElement(self, nums) -> int:
        nums = sorted(nums)
        return nums[len(nums) // 2]


if __name__ == '__main__':
    nums = [1]
    s = Solution()
    print(s.majorityElement(nums))
