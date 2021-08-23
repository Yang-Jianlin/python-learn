# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class CreateLink:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def add_head(self, val):
        Node = ListNode(val)
        Node.next = self.head.next
        self.head.next = Node

    def add_tail(self, val):
        Node = ListNode(val)
        self.tail.next = Node
        self.tail = Node


class Solution:
    def reverseKGroup(self, head: ListNode, k: int):
        if k == 1:
            return head

        nodeList = []
        while head:
            link1 = CreateLink()
            link2 = CreateLink()
            flag = 0
            for i in range(k):
                flag += 1
                link1.add_head(head.val)
                link2.add_tail(head.val)
                if head.next:
                    head = head.next
                else:
                    head = head.next
                    break
            if flag == k:
                nodeList.append(link1.head)
            else:
                nodeList.append(link2.head)

        link_res = CreateLink()
        for i in nodeList:
            new_head = i
            while new_head.next:
                link_res.add_tail(new_head.next.val)
                new_head = new_head.next
        return link_res.head.next
