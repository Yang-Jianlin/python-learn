def color_sort(nums):
    num0 = num1 = num2 = 0
    for i in nums:
        if i == 0:
            num0 += 1
        if i == 1:
            num1 += 1
        if i == 2:
            num2 += 1
    for i in range(num0):
        nums[i] = 0
    for i in range(num0, num0+num1):
        nums[i] = 1
    for i in range(num0+num1, len(nums)):
        nums[i] = 2
    return nums


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(color_sort(nums))
