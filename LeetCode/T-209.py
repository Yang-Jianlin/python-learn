class Solution:
    def minSubArrayLen(self, target, nums):
        len_nums = len(nums)
        record = []
        start = 0
        end = 0
        total = 0
        while end < len_nums:
            total += nums[end]
            while total >= target:
                record.append(end - start)
                total -= nums[start]
                start += 1
            end += 1
        if len(record) == 0:
            return 0
        else:
            return min(record) + 1


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    s = Solution()
    print(s.minSubArrayLen(target, nums))
