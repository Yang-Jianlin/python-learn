class LinkNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkList:
    def __init__(self):
        self.head = LinkNode(None, None)

    def create_link(self, val):
        node = LinkNode(val, None)
        node.next = self.head.next
        self.head.next = node


def print_link(head):
    new_head = head.next
    while new_head:
        print(new_head.val, end='-->')
        new_head = new_head.next
    print("None")


def mergeTwoLists(l1, l2):
    l3 = LinkNode(None, None)
    cur = l3
    node1 = l1.next
    node2 = l2.next
    while node1 and node2:
        if node1.val < node2.val:
            cur.next = node1
            node1 = node1.next
        else:
            cur.next = node2
            node2 = node2.next
        cur = cur.next
    if node1:
        cur.next = node1
    if node2:
        cur.next = node2
    return l3


if __name__ == '__main__':
    link1 = LinkList()
    link2 = LinkList()
    node_num1 = [4, 2, 1]
    node_num2 = [4, 3, 1]
    for i in node_num1:
        link1.create_link(i)
    print_link(link1.head.next)
    for i in node_num2:
        link2.create_link(i)
    print_link(link2.head.next)

    print_link(mergeTwoLists(link1.head, link2.head))
