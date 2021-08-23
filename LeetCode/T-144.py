class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.result
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
