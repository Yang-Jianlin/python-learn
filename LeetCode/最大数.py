def largestNumber(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if str(nums[j])+str(nums[j+1]) < str(nums[j+1])+str(nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    nums = [str(i) for i in nums]
    if int(''.join(nums)) == 0:
        return str(0)
    else:
        return ''.join(nums)


if __name__ == '__main__':
    nums = [0, 0, 0]
    print(largestNumber(nums))
