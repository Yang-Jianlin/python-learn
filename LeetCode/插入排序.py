def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


if __name__ == '__main__':
    nums = [1, 5, 8, 3, 2, 10, 7]
    print(insert_sort(nums))
