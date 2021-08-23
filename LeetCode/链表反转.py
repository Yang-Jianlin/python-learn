class LinkNode:
    def __init__(self, element):
        self.element = element
        self.next = None


class Solution:
    LinkNode = LinkNode(None)

    def __init__(self):
        self.head = LinkNode(None)

    def headInsert(self, e):
        node = LinkNode(e)
        node.next = self.head.next
        self.head.next = node

    def printNode(self):
        newNode = self.head
        while newNode.next:
            print(newNode.next.element, end='-->')
            newNode = newNode.next
        print('None')


def printNode(linkNode):
    newNode = linkNode
    while newNode.next:
        print(newNode.next.element, end='-->')
        newNode = newNode.next
    print('None')


def reverseLink(linkList):
    newHead = LinkNode(None)
    head = linkList.head
    while head.next:
        temp = head.next.element
        node = LinkNode(temp)
        node.next = newHead.next
        newHead.next = node
        head = head.next
    return newHead


if __name__ == '__main__':
    s = Solution()
    for i in range(0, 6):
        s.headInsert(i)
    s.printNode()

    printNode(reverseLink(s))
