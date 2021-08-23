class Solution:
    def rotate1(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n

        num1 = nums[:n - k]
        num2 = nums[n - k:]
        num2.extend(num1)
        nums.clear()
        nums.extend(num2)

    def rotate2(self, nums, k):
        n = len(nums)
        k = k % n
        while k:
            nums.insert(0, nums.pop())
            k -= 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate1(nums, k)
    print(nums)
