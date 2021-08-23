class Solution(object):
    def pancakeSort(self, A):
        result = []
        for i in range(len(A) - 1, -1, -1):
            index = A.index(max(A[:i + 1]))
            A[:index + 1] = A[:index + 1][::-1]
            result.append(index + 1)
            A[0:i + 1] = A[0:i + 1][::-1]
            result.append(i + 1)
        return result


if __name__ == '__main__':
    A = [3, 2, 4, 1]
    s = Solution()
    print(s.pancakeSort(A))
