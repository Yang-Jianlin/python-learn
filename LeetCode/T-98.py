class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True
        elif root.val > root.right.val or root.val < root.left.val:
            return False
        else:
            return self.isValidBST(root.left) and self.isValidBST(root.right)


class Solution:
    def __init__(self):
        self.re = []

    def isValidBST(self, root: TreeNode) -> bool:
        # return self.helper(root)
        self.inorder(root)
        re_sort = sorted(self.re, reverse=True)
        if re_sort == self.re:
            return True
        else:
            return False

    def helper(self, node, lower=float('-inf'), upper=float('inf')) -> bool:
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        return helper(node.right, node.val, upper) and helper(node.left, lower, node.val)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.re.append(root.val)
        self.inorder(root.right)
