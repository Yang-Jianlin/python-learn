class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CreateListNode:
    def __init__(self):
        self.head = ListNode(0, None)
        self.tail = self.head

    def tail_insert(self, val):
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def print_node(self):
        new_head = self.head
        while new_head.next:
            print(new_head.next.element, end='-->')
            new_head = new_head.next
        print('None')


class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return
        preNode = head
        postNode = head.next
        while postNode:
            if preNode.val == postNode.val:
                postNode = postNode.next
            else:
                preNode.next = postNode
                preNode = postNode
                postNode = postNode.next
        else:
            preNode.next = None

        return head
