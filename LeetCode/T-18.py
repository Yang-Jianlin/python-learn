class Solution:
    def fourSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                current = j
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