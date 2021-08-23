def choose_sort(nums):
    for i in range(0, len(nums)):
        min_position = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_position]:
                min_position = j
        if i != min_position:
            nums[i], nums[min_position] = nums[min_position], nums[i]
    return nums


if __name__ == '__main__':
    nums = [1, 5, 8, 3, 2, 10, 7]
    print(choose_sort(nums))
