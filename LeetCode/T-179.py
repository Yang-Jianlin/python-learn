class Solution:
    def largestNumber(self, nums):
        str_nums = [str(i) for i in nums]
        for i in range(0, len(nums)-1):
            for j in range(0, len(nums)-i-1):
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
        if int(''.join(str_nums)) == 0:
            return str(0)
        else:
            return ''.join(str_nums)


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    s = Solution()
    print(s.largestNumber(nums))
