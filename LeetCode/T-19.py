class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CreateList:
    def __init__(self):
        self.head = ListNode(0, None)
        self.tail = self.head

    def createHeadNode(self, val):
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node

    def createTailNode(self, val):
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def printNode(self):
        head = self.head
        while head.next:
            print(head.next.val, end='-->')
            head = head.next
        print('None')


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head1 = head
        head2 = head.next
        while n > 0:
            n -= 1
            head2 = head2.next
        while head2:
            head1 = head1.next
            head2 = head2.next
        head1.next = head1.next.next
        return head
