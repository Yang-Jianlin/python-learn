class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            second_index = i + 1
            end_index = len(nums) - 1
            while second_index < end_index:
                sum_num = nums[i] + nums[second_index] + nums[end_index]
                if sum_num == target:
                    return sum_num
                res.append(sum_num)
                if sum_num > target:
                    end_index -= 1
                else:
                    second_index += 1

        return self.result(res, target)

    def result(self, res, target):
        best = 10 ** 7
        for i in res:
            if abs(i - target) < abs(best - target):
                best = i
        return best


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(s.threeSumClosest(nums, target))
