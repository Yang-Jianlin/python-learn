class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_num = max(candies)
        for i in candies:
            if i + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)

        return result


if __name__ == '__main__':
    s = Solution()
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(s.kidsWithCandies(candies, extraCandies))
