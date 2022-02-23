from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def delete(curr: Optional[ListNode]) -> int:
            if not curr:
                return 1

            num_from_last = delete(curr.next)

            if num_from_last == n + 1 and curr.next:
                curr.next = curr.next.next

            return num_from_last + 1

        num_from_last = delete(head)

        if num_from_last == n + 1:
            return head.next

        return head

def test_happy_path():
    input = ListNode(1, ListNode(2, ListNode(3)))
    expected = ListNode(1, ListNode(2))
    actual = Solution().removeNthFromEnd(input, 1)

    assert actual.val == expected.val
    assert actual.next.val == expected.next.val
    assert not actual.next.next

def test_remove_middle():
    input = ListNode(1, ListNode(2, ListNode(3)))
    expected = ListNode(1, ListNode(3))
    actual = Solution().removeNthFromEnd(input, 2)

    assert actual.val == expected.val
    assert actual.next.val == expected.next.val
    assert not actual.next.next

def test_remove_end():
    input = ListNode(1, ListNode(2, ListNode(3)))
    expected = ListNode(2, ListNode(3))
    actual = Solution().removeNthFromEnd(input, 3)

    assert actual.val == expected.val
    assert actual.next.val == expected.next.val
    assert not actual.next.next


if __name__ == "__main__":
    test_happy_path()

