class Solution:
    def __init__(self):
        self.time = 0

    def move(self, n, a, b, c):
        if n == 1:
            self.print(n, a, c)
        else:
            self.move(n - 1, a, c, b)
            self.move(1, a, b, c)
            self.move(n - 1, b, a, c)

    def print(self, n, a, c):
        self.time += 1
        print('第{}次操作：将第{}个圆盘从{}-->{}'.format(self.time, n, a, c))


if __name__ == '__main__':
    s = Solution()
    n = 3
    a = 'A'
    b = 'B'
    c = 'C'
    s.move(3, a, b, c)
