def rapid_sort(nums, low, high):
    if low >= high:
        return nums
    i = low
    j = high
    key = nums[i]
    while i < j:
        while i < j and key <= nums[j]:
            j -= 1
        nums[i] = nums[j]
        while i < j and key >= nums[i]:
            i += 1
        nums[j] = nums[i]
    nums[i] = key
    rapid_sort(nums, low, i-1)
    rapid_sort(nums, i+1, high)


def bubble_sort(nums):
    for i in range(0, len(nums)-1):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def choose_sort(nums):
    for i in range(0, len(nums)):
        min_position = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_position]:
                min_position = j
        if i != min_position:
            nums[i], nums[min_position] = nums[min_position], nums[i]
        return nums


def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


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
    nums1 = [50, 25, 67, 12, 23, 90, 69]
    rapid_sort(nums1, 0, len(nums1)-1)
    print(nums1)

    nums2 = [50, 25, 67, 12, 23, 90, 69]
    bubble_sort(nums2)
    print(nums2)

    nums3 = [50, 25, 67, 12, 23, 90, 69]
    bubble_sort(nums3)
    print(nums3)
