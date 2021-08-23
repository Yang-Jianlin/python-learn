class Solution:
    def shuffle(self, nums, n: int):
        j = n - 1
        for i in range(n, len(nums)):
            nums.insert(i - j, nums[i])
            nums.pop(i + 1)
            j -= 1
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(s.shuffle(nums, n))
