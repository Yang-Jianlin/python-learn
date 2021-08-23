def rapid_sort(nums, low, high):
    if low >= high:
        return nums
    i = low
    j = high
    key = nums[i]
    while i < j:
        while i < j and nums[j] >= key:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= key:
            i += 1
        nums[j] = nums[i]
    nums[i] = key
    rapid_sort(nums, low, i-1)
    rapid_sort(nums, i+1, high)


if __name__ == '__main__':
    nums = [1, 5, 8, 3, 2, 10, 7]
    rapid_sort(nums, 0, len(nums)-1)
    print(nums)
