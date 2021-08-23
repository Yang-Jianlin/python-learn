class LinkList:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.head = self.ListNode(None)
        self.tail = self.head

    def addTail(self, e):
        Node = self.ListNode(e)
        self.tail.next = Node
        self.tail = Node

    def printLinkList(self, Link):
        headNode = Link.head
        while headNode.next is not None:
            print(headNode.next.val, end='-->')
            headNode = headNode.next
        print('None')

    def searchNode(self, e):
        headNode = self.head
        while headNode.next:
            if headNode.next.val == e:
                return headNode.next
            headNode = headNode.next

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    Link = LinkList()
    for i in range(0, 5):
        Link.addTail(i)
    Link.printLinkList(Link)

    node = Link.searchNode(1)
    Link.deleteNode(node)
    Link.printLinkList(Link)
