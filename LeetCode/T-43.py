class Solution(object):
    def multiply(self, num1, num2):
        num1 = self.num_str(num1)
        num2 = self.num_str(num2)
        res = num1 * num2
        return str(res)

    def num_str(self, num):
        if num == '0':
            return 0
        res, b = 0, 1
        for i in range(len(num)-1, -1, -1):
            res = int(num[i]) * b + res
            b *= 10
        return res


if __name__ == '__main__':
    num1 = "3"
    num2 = "6"
    s = Solution()
    print(s.multiply(num1, num2))
