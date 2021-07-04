# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        sumInTree = False
        def dfs(node, sofar=0):
            nonlocal sumInTree
            if node is None:
                sumInTree |= sofar == sum
                return

            dfs(node.left, sofar + node.val)
            dfs(node.right, sofar + node.val)

        dfs(root)
        return sumInTree
    
    def hasPathSum2(self, root: TreeNode, sum: int) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return [node.val]

            left = []
            right = []
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            all_results = left + right
            return list(map(lambda result: result + node.val, all_results))

        return sum in dfs(root)

        

sol = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(sol.hasPathSum1(root, 22))
print(sol.hasPathSum2(root, 22))