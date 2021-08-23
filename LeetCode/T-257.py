class Solution:
    def dfs(root, res, str_):
        if not root:
            return
        else:
            str_ += str(root.val)
            self.dfs(root.left, res, str_+'->')
            self.dfs(root.right, res, str_+'->')
        if not root.left and not root.right:
            res.append(str_)

    def binaryTreePaths(self, root):
        res = []
        str1 = ''
        self.dfs(root, res)
        return res
