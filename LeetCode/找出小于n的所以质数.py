class Solution:
    def methmod(self, n):
        result = []
        for i in range(2, n):
            k = 1
            for j in range(2, i+1):
                k += 1
                if i % j == 0:
                    break
            if k >= i:
                result.append(i)
        return result


if __name__ == '__main__':
    s = Solution()
    n = 100
    print(s.methmod(n))
