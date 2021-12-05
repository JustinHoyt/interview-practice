# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = root
        tail = root
        
        def find_range(curr):
            leftmost = 0
            rightmost = 0

            if curr.val < head.val: head = curr
            if curr.val > tail.val: tail = curr

            if curr.left:
                left_range = find_range(curr.left)
                curr.left = left_range[1]
                left_range[1].right = curr.left
                leftmost = left_range[0]
            else:
                leftmost = curr
            
            if curr.right:
                right_range = find_range(curr.right)
                curr.right = right_range[0]
                right_range[0].left = curr.right
                rightmost = right_range[1]
            else:
                rightmost = curr

            return (leftmost, rightmost)

        find_range(root)
        head.left = tail
        tail.right = head
        return head
