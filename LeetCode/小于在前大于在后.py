def target_sort(nums, target):
    n = nums.index(target)
    nums[0], nums[n] = nums[n], nums[0]
    start = 0
    end = len(nums) - 1
    key = nums[0]
    while start < end:
        while start < end and nums[end] >= key:
            end -= 1
        nums[start] = nums[end]
        while start < end and nums[start] <= key:
            start += 1
        nums[end] = nums[start]
        nums[start] = key
    return nums


if __name__ == '__main__':
    nums = [4, 5, 3, 8, 2, 9, 10, 1]
    print(target_sort(nums, target=5))
