class SinLinkedList:
    # 节点的数据结构，包含一个值和一个指针
    class Node:
        __slots__ = {'_element', '_next'}

        def __init__(self, element):
            self._element = element
            self._next = None

    # head表示头节点，tail用于尾插法
    # 初始化时头节点的值设置为空，头节点的下一个也是空
    def __init__(self):
        self._head = self.Node(None)
        self._tail = self._head
        self._size = 0

    # 尾插法创建链表，输出的数是输入的顺序
    # 头插法就是将数据始终插入头节点后面
    def add_node_tail(self, e):
        Node = self.Node(e)
        self._tail._next = Node
        self._tail = Node
        self._size += 1

        return self._tail

    # 删除链表的某一个元素
    # 删除元素，需要知道至少两个节点指针，这样才能将所删元素跳过
    def remove_node(self, e):
        pre_node = self._head
        now_node = self._head._next
        while now_node is not None:
            if now_node._element == e:
                pre_node._next = now_node._next
                now_node = pre_node._next
            else:
                pre_node = now_node
                now_node = now_node._next

    # 输出链表节点
    # 如论何时，链表最好保持头节点指针不动，所以下面now_node = self._head
    def print_link_node(self):
        now_node = self._head
        while now_node._next is not None:
            print(now_node._next._element, end='-->')
            now_node = now_node._next
        print('None')


if __name__ == '__main__':
    link = SinLinkedList()
    num = []
    for i in num:
        link.add_node_tail(i)
    link.print_link_node()
    link.remove_node(1)
    link.print_link_node()
