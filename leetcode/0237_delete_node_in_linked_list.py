class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node, target):
        while node:
            if node.next and node.next.val == target:
                node.next = node.next.next

            node = node.next

linked_list = ListNode(3)
linked_list.next = ListNode(2)
linked_list.next.next = ListNode(9)
linked_list.next.next.next = ListNode(4)
# linked_list.next.next.next.next = ListNode(5)

Solution().deleteNode(linked_list, 4);
print(linked_list.next.next.next)