class Solution:
    def subtractProductAndSum(self, n):
        i = 1
        j = i * 10
        add = 0
        multi = 1

        while True:
            each = n % j // i
            add = add + each
            multi = multi * each
            if j > n:
                break
            else:
                i = j
                j = i * 10

        return multi - add


if __name__ == '__main__':
    s = Solution()
    n = 4421
    print(s.subtractProductAndSum(n))
