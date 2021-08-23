class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        root_left = root.left
        root_right = root.right
        l_res = []
        r_res = []
        self.leftTree(root_left, l_res)
        self.rightTree(root_right, r_res)
        return l_res == r_res

    def leftTree(self, root, l_res):
        if not root:
            l_res.append(' ')
            return
        l_res.append(root.val)
        self.leftTree(root.left, l_res)
        self.leftTree(root.right, l_res)

    def rightTree(self, root, r_res):
        if not root:
            r_res.append(' ')
            return
        r_res.append(root.val)
        self.rightTree(root.right, r_res)
        self.rightTree(root.left, r_res)
