class Solution:
    # 先分解出质因数
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            ugly = [2, 3, 5]
            result = []
            while n > 1:
                for i in range(2, n + 1):
                    if n % i == 0:
                        n //= i
                        result.append(i)
                        break
            r = set(result)
            for i in r:
                if i not in ugly:
                    return False
            else:
                return True

    # 直接用丑数的定义做
    def isUgly2(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        else:
            ugly = [2, 3, 5]
            while n > 1:
                for i in ugly:
                    if n % i == 0:
                        n = n // i
                        break
                else:
                    return False
            else:
                return True


if __name__ == '__main__':
    s = Solution()
    n = 7
    print(s.isUgly(n))
    print(s.isUgly2(n))
