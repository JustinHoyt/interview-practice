from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        def max_depth_rec(curr: TreeNode, height):
            nonlocal max_depth
            if not curr:
                max_depth = max(max_depth, height)
                return
            
            max_depth_rec(curr.left, height + 1)
            max_depth_rec(curr.right, height + 1)

        max_depth_rec(root, 0)
        return max_depth


def test_happy_path():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3


if __name__ == "__main__":
    test_happy_path()