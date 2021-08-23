from LeetCode.链表排序 import CreateLink
from LeetCode.链表排序 import LinkNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        newlink = LinkNode(None)
        new_l1 = l1.next
        new_l2 = l2.next
        num_l1 = 0
        num_l2 = 0
        i = 1
        j = 1
        while new_l1:
            num_l1 = num_l1 + new_l1.element * i
            i *= 10
            new_l1 = new_l1.next
        while new_l2:
            num_l2 = num_l2 + new_l2.element * j
            j *= 10
            new_l2 = new_l2.next
        num_sum = num_l1 + num_l2
        num = list(str(num_sum))
        for i in num:
            node = LinkNode(int(i))
            node.next = newlink.next
            newlink.next = node
        return newlink


def print_node(node):
    new_head = node
    while new_head.next:
        print(new_head.next.element, end='-->')
        new_head = new_head.next
    print('None')


if __name__ == '__main__':
    link1 = CreateLink()
    link2 = CreateLink()
    nums1 = [2, 4, 3]
    nums2 = [5, 6, 4]
    for i in nums1:
        link1.add_tail(i)
    for j in nums2:
        link2.add_tail(j)

    s = Solution()
    print_node(s.addTwoNumbers(link1.head, link2.head))
