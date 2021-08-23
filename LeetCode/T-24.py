class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        if not head:
            return head
        if not head.next:
            return head

        preNode = new_head
        inNode = head
        postNode = head.next
        flag = 1
        while postNode and inNode:
            if flag == 1:
                flag = 0
                preNode.next = postNode
                inNode.next = postNode.next
                postNode.next = inNode
            elif flag == 0:
                flag = 1
                preNode.next = inNode
                postNode.next = inNode.next
                inNode.next = postNode

            if not inNode.next or not postNode.next or not inNode.next.next or not postNode.next.next:
                break
            preNode = preNode.next.next
            inNode = inNode.next.next
            postNode = postNode.next.next

        return new_head.next
