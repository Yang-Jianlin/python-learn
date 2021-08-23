class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        global x_depth, y_depth, x_parents, y_parents
        if not root:
            return False
        queue = [(1, root, None)]
        while queue:
            depth, node, parents = queue.pop(0)
            if node.val == x:
                x_depth = depth
                x_parents = parents
            if node.val == y:
                y_depth = depth
                y_parents = parents
            if node.left:
                queue.append((depth + 1, node.left, node))
            if node.right:
                queue.append((depth + 1, node.right, node))
        return x_depth == y_depth and x_parents != y_parents
