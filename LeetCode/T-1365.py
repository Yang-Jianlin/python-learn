class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            result.append(count)
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [8, 1, 2, 2, 3]
    print(s.smallerNumbersThanCurrent(nums))
