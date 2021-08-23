class Solution:
    def generateParenthesis(self, n: int):
        re = []

        def dfs(left_num, right_num, string):
            if left_num + right_num == 2 * n:
                re.append(string)
                return
            if left_num < n:
                dfs(left_num+1, right_num, string+'(')
            if right_num < left_num:
                dfs(left_num, right_num+1, string+')')

        dfs(1, 0, '(')
        return re
