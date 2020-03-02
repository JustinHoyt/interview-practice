class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        leave_sum = 0
        deepest_level = 1

        def dfs(node, level=1):
            nonlocal deepest_level
            nonlocal leave_sum

            if not node:
                return

            if deepest_level == level:
                leave_sum += node.val
            elif level > deepest_level:
                leave_sum = node.val
                deepest_level = level

            dfs(node.left, level+1)
            dfs(node.right, level+1)

        if root:
            dfs(root)
        return leave_sum


root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(-1)
root.left.left.right = TreeNode(100)
root.left.right = TreeNode(2)
root.right = TreeNode(7)

sol = Solution()
print(sol.deepestLeavesSum(root))

