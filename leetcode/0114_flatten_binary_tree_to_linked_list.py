from typing import *
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def append_right(node, right):
            while node.right:
                node = node.right
            node.right = right


        def flatten_rec(node: TreeNode):
            if not node: return

            temp_right = node.right
            if node.left:
                node.right = node.left
                node.left = None
                append_right(node.right, temp_right)

            flatten_rec(node.right)
        
        flatten_rec(root)


def test_happy_path():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten(root) 
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    assert root.right.right.right.val == 4
    assert root.right.right.right.right.val == 5
    assert root.right.right.right.right.right.val == 6


if __name__ == "__main__":
    test_happy_path()