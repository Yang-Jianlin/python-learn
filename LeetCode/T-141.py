class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        fastNode = head
        slowNode = head
        while fastNode:
            if fastNode is None:
                return False
            fastNode = fastNode.next.next
            slowNode = slowNode.next
            if fastNode == slowNode:
                return True
        return False
