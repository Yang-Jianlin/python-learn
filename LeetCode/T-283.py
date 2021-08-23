class Solution:
    def moveZeroes(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            i += 1
        return nums

    def moveZeroes2(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)
        return nums

    def moveZeroes3(self, nums):
        i = 0
        j = len(nums) - 1
        while i < j:
            num = nums[j]
            if nums[i] == 0:
                nums[j] = nums[i]
                nums.insert(j, num)
                nums.remove(0)
                j -= 1
            else:
                i += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    # print(s.moveZeroes(nums))
    print(s.moveZeroes3(nums))
