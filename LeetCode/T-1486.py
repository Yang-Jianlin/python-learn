def xorOperation(n: int, start: int):
    nums = []
    for i in range(n):
        nums.append(start + 2*i)

    s = nums[0]
    nums.pop(0)
    for j in nums:
        s = s ^ j
    return s


if __name__ == '__main__':
    print(xorOperation(10, 5))
