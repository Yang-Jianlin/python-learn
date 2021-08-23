class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        array = [[0 for _ in range(0, len2+1)] for _ in range(0, len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    array[i][j] = array[i-1][j-1] + 1
                else:
                    array[i][j] = max(array[i-1][j], array[i][j-1])
        max_len = array[len1][len2]
        return max_len


if __name__ == '__main__':
    s = Solution()
    text1 = 'abcdef'
    text2 = 'bcxdef'
    print(s.longestCommonSubsequence(text1, text2))
