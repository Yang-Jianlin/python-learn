class LinkNode:
    def __init__(self, element):
        self.element = element
        self.next = None


class CreateLink:
    def __init__(self):
        self.head = LinkNode(None)
        self.tail = self.head

    def add_head(self, e):
        Node = LinkNode(e)
        Node.next = self.head.next
        self.head.next = Node

    def add_tail(self, e):
        Node = LinkNode(e)
        self.tail.next = Node
        self.tail = Node

    def print_node(self):
        new_head = self.head
        while new_head.next:
            print(new_head.next.element, end='-->')
            new_head = new_head.next
        print('None')


class LinkMethod:
    def count_link(self, Node):
        new_head = Node
        count = 0
        while new_head.next:
            count += 1
            new_head = new_head.next
        return count

    def sort_link(self, Node):
        firstNode = Node.next
        second_Node = firstNode
        while firstNode:
            while firstNode.next:
                if firstNode.element > firstNode.next.element:
                    temp = firstNode.element
                    firstNode.element = firstNode.next.element
                    firstNode.next.element = temp
                firstNode = firstNode.next
            firstNode = second_Node.next
            second_Node = firstNode

    def reverse_link(self, Node):
        pass

    def union_link(self, Node1, Node2):
        pass


if __name__ == '__main__':
    node = [2, 4, 1, 8, 9, 3]
    LinkList1 = CreateLink()
    LinkList2 = CreateLink()
    for i in node:
        LinkList1.add_head(i)
    LinkList1.print_node()
    for j in node:
        LinkList2.add_tail(j)
    LinkList2.print_node()

    LinkMethod = LinkMethod()
    print(LinkMethod.count_link(LinkList1.head))

    LinkMethod.sort_link(LinkList1.head)
    LinkList1.print_node()
