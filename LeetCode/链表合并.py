# 一个链表，奇数位升序偶数位降序，让链表变成升序的
from LeetCode.链表排序 import CreateLink


class LinkNode:
    def __init__(self, element):
        self.element = element
        self.next = None


class LinkList:
    def __init__(self):
        self.head = LinkNode(None)
        self.tail = LinkNode(None)
        self.head_tail = self.tail

    def sort_link(self, headNode):
        num = 0
        after_head = headNode.next
        while after_head:
            num += 1
            if num % 2 == 0:
                node = LinkNode(after_head.element)
                node.next = self.head.next
                self.head.next = node
            else:
                node = LinkNode(after_head.element)
                self.tail.next = node
                self.tail = node
            after_head = after_head.next


def union_link(node1, node2):
    head = LinkNode(None)
    cur = head

    cur1 = node1.next
    cur2 = node2.next
    while cur1 and cur2:
        if cur1.element <= cur2.element:
            cur.next = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur2 = cur2.next
        cur = cur.next

    if cur1 is not None:
        cur.next = cur1

    if cur2 is not None:
        cur.next = cur2
    return head


def print_node(node):
    new_head = node
    while new_head.next:
        print(new_head.next.element, end='-->')
        new_head = new_head.next
    print('None')


if __name__ == '__main__':
    nums = [1, 8, 2, 7, 3, 6, 4, 5]
    link = CreateLink()
    for i in nums:
        link.add_tail(i)
    link.print_node()

    link_sort = LinkList()
    link_sort.sort_link(link.head)

    print_node(union_link(link_sort.head_tail, link_sort.head))
