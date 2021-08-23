class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array_path = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            array_path[i][0] = 1
        for j in range(n):
            array_path[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                array_path[i][j] = array_path[i-1][j] + array_path[i][j-1]
        return array_path[m-1][n-1]
