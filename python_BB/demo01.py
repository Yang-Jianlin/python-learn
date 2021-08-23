import random


def insert_half(nums, num_insert, low, high):
    while low <= high:
        mid = (low+high) // 2
        if num_insert > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    nums.insert(low, num_insert)
    return nums


if __name__ == '__main__':
    nums = []
    for i in range(8):
        nums.append(random.randint(1, 100))
    print(nums)

    nums.sort()
    num_insert = int(input("please enter num:"))
    print(insert_half(nums, num_insert, 0, len(nums)-1))
