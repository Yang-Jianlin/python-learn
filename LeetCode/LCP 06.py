import math


class Solution:
    def minCount(self, coins):
        count = 0
        for i in coins:
            num = i / 2
            count = count + math.ceil(num)

        return count


if __name__ == '__main__':
    s = Solution()
    conis = [2,3,10]
    print(s.minCount(conis))
