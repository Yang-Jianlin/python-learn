class Solution:
    def method(self, num_list):
        num_new = sorted(num_list)
        n = len(num_list) // 2
        return num_new[n]


if __name__ == '__main__':
    s = Solution()
    num_list = [1, 3, 8, 9, 3, 3, 4, 4, 6, 4, 4, 4]
    print(s.method(num_list))
