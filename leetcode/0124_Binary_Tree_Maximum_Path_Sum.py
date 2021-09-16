class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode):
        max_path = root.val if root else 0
        def max_path_sum(node: TreeNode):
            nonlocal max_path
            if not node: return 0

            max_left = max_path_sum(node.left)
            max_right = max_path_sum(node.right)

            max_branch = max(
                max_left + node.val,
                max_right + node.val,
                node.val
            )
            max_path = max(
                max_left + node.val + max_right,
                max_branch,
                max_path
            )
            return max_branch

        max_path_sum(root)
        return max_path


'''
     -10
  9       20
// //   15   7
'''
def test_happy_path():
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = None
    root.left.right = None
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxPathSum(root) == 42

'''
     -1
  -2       10
-6  //   -3  -6
'''
def test_negative_sums():
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(-6)
    root.left.right = None
    root.right.left = TreeNode(-3)
    root.right.right = TreeNode(-6)
    assert Solution().maxPathSum(root) == 10

if __name__ == "__main__":
    test_happy_path()