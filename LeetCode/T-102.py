class Solution:
    def levelOrder(self, root):
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
