import heapq


def heap_sort(nums):
    result = []
    for i in range(len(nums)):
        heapq.heapify(nums)
        result.append(nums[0])
        nums.remove(nums[0])
    return result


if __name__ == '__main__':
    nums = [1, 5, 2, 8, 4, 3]
    print(heap_sort(nums))
