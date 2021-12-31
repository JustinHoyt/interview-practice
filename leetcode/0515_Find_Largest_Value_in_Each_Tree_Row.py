
# Definition for a binary tree node.
from typing import Deque
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        queue = Deque()
        queue.appendleft((0, root))
        results = []
        high = -math.inf
        level = 0
        while queue:
            node_level, node = queue.pop()
            if node_level > level:
                results.append(high)
                high = -math.inf
                level += 1
            high = max(node.val, high)
            
            node.left and queue.appendleft((level + 1, node.left))
            node.right and queue.appendleft((level + 1, node.right))

        results.append(high)
        return results



def test_happy_path():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = None
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    assert Solution().largestValues(root) == [1, 3, 7]

def test_happy_path_2():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.left = None
    root.right.right = TreeNode(9)
    assert Solution().largestValues(root) == [1, 3, 9]

if __name__ == "__main__":
    test_happy_path()