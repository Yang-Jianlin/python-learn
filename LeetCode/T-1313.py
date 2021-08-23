class Solution:
    def decompressRLElist(self, nums):
        l = []
        for i in range(0, len(nums)):
            if 2 * i + 1 > len(nums):
                break
            a = nums[2 * i]
            while a:
                l.append(nums[2 * i + 1])
                a -= 1
        return l


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 3]
    print(s.decompressRLElist(nums))
