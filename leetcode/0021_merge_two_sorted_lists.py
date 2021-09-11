from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        l3: Optional[ListNode] = None
        if l1.val < l2.val:
            l3 = ListNode(l1.val)
            l1 = l1.next
        else:
            l3 = ListNode(l2.val)
            l2 = l2.next
        
        l3_head = l3

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next

        for pointer in [l1, l2]:
            while pointer:
                l3.next = ListNode(pointer.val)
                l3 = l3.next
                pointer = pointer.next
        
        return l3_head


    def equals(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
        while l1 and l2:
            if l1.val != l2.val: return False
            l1 = l1.next
            l2 = l2.next
        
        if l1 or l2: 
            return False
        return True


def test_happy_path():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    expected = ListNode(1)
    expected.next = ListNode(1)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(3)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(4)
    list_helper = Solution()
    actual = list_helper.mergeTwoLists(l1, l2)
    assert list_helper.equals(actual, expected) == True


if __name__ == "__main__":
    test_happy_path()