def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums


if __name__ == '__main__':
    nums = [3, 1, 2, 10, 1]
    print(runningSum(nums))
