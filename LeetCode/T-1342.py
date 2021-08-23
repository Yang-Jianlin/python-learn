class Solution:
    def numberOfSteps(self, num):
        count = 0
        while num != 0:
            count += 1
            if num % 2 == 0:
                num = num/2
            else:
                num = num-1
        return count


if __name__ == '__main__':
    s = Solution()
    num = 123
    print(s.numberOfSteps(num))
