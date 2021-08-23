def add_num(nums, target):
    sort_nums = sorted(nums)
    result = []

    i = 0
    j = len(nums) - 1
    while i < j:
        s = sort_nums[i] + sort_nums[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            result.append([nums.index(sort_nums[i]), nums.index(sort_nums[j])])
            i += 1

    return result


if __name__ == '__main__':
    nums = [2, 1, 6, 7, 5, 3, 4]
    target = 6
    print(add_num(nums, target))
