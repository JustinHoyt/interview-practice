from typing import *
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid_bst(node: TreeNode, left_bound, right_bound):
            if not node: 
                return True
            if left_bound < node.val < right_bound:
                return is_valid_bst(node.left, left_bound, node.val) \
                    and is_valid_bst(node.right, node.val, right_bound)
            return False

        return is_valid_bst(root, float('-inf'), float('inf'))

    def isValidBSTInOrderTraversal(self, root: TreeNode) -> bool:
        self.prev = -math.inf
        def valid_bst(node: TreeNode):
            if not node: 
                return True
            
            if not valid_bst(node.left):
                return False
            if self.prev > node.val:
                return False
            self.prev = node.val
            return valid_bst(node.right)

        return valid_bst(root)


def test_happy_path():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(14)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(60)
    assert Solution().isValidBST(root) == True
    assert Solution().isValidBSTInOrderTraversal(root) == True

def test_invalid_bst():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(14)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(60)
    assert Solution().isValidBST(root) == False
    assert Solution().isValidBSTInOrderTraversal(root) == False

if __name__ == "__main__":
    test_happy_path()