def numIdenticalPairs(nums):
    count = 0
    for i in range(0, len(nums)):
        j = i + 1
        for y in range(j, len(nums)):
            if nums[i] == nums[y]:
                count += 1
    return count


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    print(numIdenticalPairs(nums))
