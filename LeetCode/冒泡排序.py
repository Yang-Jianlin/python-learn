def bubble_sort(nums):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [1, 5, 8, 3, 2, 10, 7]
    print(bubble_sort(nums))
