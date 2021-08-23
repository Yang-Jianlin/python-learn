class Solution:
    def twoSum(self, nums, target):
        sort_nums = sorted(nums)
        result = []

        i = 0
        j = len(nums) - 1
        while i < j:
            s = sort_nums[i] + sort_nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                start = nums.index(sort_nums[i])
                end = nums.index(sort_nums[j])
                if start != end:
                    result.append([start, end])
                else:
                    end = nums.index(sort_nums[j], start+1, len(nums))
                    result.append([start, end])
                i += 1

        return result


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3]
    target = 6
    print(s.twoSum(nums, target))
