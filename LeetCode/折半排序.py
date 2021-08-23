def half_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        low = 0
        high = i-1
        while low <= high:
            mid = (high+low)//2
            if key < nums[mid]:
                high = mid - 1
            if key >= nums[mid]:
                low = mid + 1
        j = i-1
        while j >= low:
            nums[j+1] = nums[j]
            j -= 1
        nums[low] = key
    return nums


if __name__ == '__main__':
    nums = [1, 5, 8, 3, 2, 10, 7]
    print(half_sort(nums))
