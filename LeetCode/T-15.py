class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            current = i
            before_needle = current + 1
            after_needle = len(nums) - 1
            while before_needle < after_needle:
                s = nums[current] + nums[before_needle] + nums[after_needle]
                if s < 0:
                    before_needle += 1
                    while before_needle < after_needle and nums[before_needle] == nums[before_needle - 1]:
                        before_needle += 1
                elif s > 0:
                    after_needle -= 1
                    while after_needle > before_needle and nums[after_needle] == nums[after_needle + 1]:
                        after_needle -= 1
                else:
                    if [nums[current], nums[before_needle], nums[after_needle]] not in result:
                        result.append([nums[current], nums[before_needle], nums[after_needle]])
                    before_needle += 1
                    after_needle -= 1
                    while before_needle < after_needle and nums[before_needle] == nums[before_needle - 1]:
                        before_needle += 1
                    while after_needle > before_needle and nums[after_needle] == nums[after_needle + 1]:
                        after_needle -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
