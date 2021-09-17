from typing import *

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def recurse(node):
            nonlocal lca
            if not node:
                return False

            left = recurse(node.left)
            right = recurse(node.right)

            if left and right:
                lca = node
            
            if (left or right) and (node.val == p.val or node.val == q.val):
                lca = node
            if (left or right) or (node.val == p.val or node.val == q.val):
                return True
            return False
        
        recurse(root)
        return lca

'''
     -10
  9       20
// //   15   8
'''
def test_happy_path():
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)
    assert Solution().lowestCommonAncestor(root, root.right.left, root.right.right).val == 20

def test_lca_is_argument():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.left.left = None
    root.left.left.right = None
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    assert Solution().lowestCommonAncestor(root, root.left, root.left.right.right).val == 5

def test_smallest_tree():
    root = TreeNode(-10)
    root.left = TreeNode(9)
    assert Solution().lowestCommonAncestor(root, root, root.left).val == -10


if __name__ == "__main__":
    test_lca_is_argument()