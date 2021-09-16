from typing import *

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        view: List[int] = []
        max_height = 0

        def right_side_view_rec(curr: TreeNode, height) -> None:
            nonlocal max_height

            if not curr:
                return
            
            if height > max_height:
                view.append(curr.val)
                max_height += 1
            
            right_side_view_rec(curr.right, height + 1)
            right_side_view_rec(curr.left, height + 1)

        right_side_view_rec(root, 1)

        return view


'''
     -10
  9       20
// //   15   //

'''
def test_happy_path():
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = None
    assert Solution().rightSideView(root) == [-10, 20, 15]

def test_empty_tree():
    root = None
    assert Solution().rightSideView(root) == []


if __name__ == "__main__":
    test_happy_path()