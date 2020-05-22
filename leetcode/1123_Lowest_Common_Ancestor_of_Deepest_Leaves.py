class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lcaDeepestLeaves(self, root):
        def helper(node):
            if not node:
                return 0, None

            left_height, left_lca = helper(node.left)
            right_height, right_lca = helper(node.right)
            if left_height > right_height:
                return 1 + left_height, left_lca
            elif right_height > left_height:
                return 1 + right_height, right_lca
            else:
                return 1 + left_height, node

        _, lca = helper(root)
        return lca

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
print(Solution().lcaDeepestLeaves(tree).val)