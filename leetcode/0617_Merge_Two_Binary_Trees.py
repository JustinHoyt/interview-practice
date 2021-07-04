# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        root_node = TreeNode(0)

        if not t1 and not t2:
            return None
            
        root_node = TreeNode(0)
        if t1:
            root_node.val += t1.val
        if t2:
            root_node.val += t2.val
            
        root_node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root_node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return root_node

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

sol = Solution()
print(sol.mergeTrees(root1, root2))