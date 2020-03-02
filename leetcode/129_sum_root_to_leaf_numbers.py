class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def sumNumbers(self, root):
        result = 0

        def dfs(node, num_sofar=''):
            nonlocal result

            if not node.left and not node.right:
                result += int(num_sofar + str(node.val))
                return

            if node.left:
                dfs(node.left, num_sofar + str(node.val))
            if node.right:
                dfs(node.right, num_sofar + str(node.val))

        if root:
            dfs(root)
        return result


class Solution2:
    def sumNumbers(self, root):
        def dfs(node, sofar=0):
            if not node:
                return 0

            if not node.right and not node.left:
                return sofar * 10 + node.val

            return (dfs(node.left, sofar * 10 + node.val) +
                    dfs(node.right, sofar * 10 + node.val))

        return dfs(root)


root = TreeNode(4)
root.left = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
root.right = TreeNode(0)

sol = Solution()
print(sol.sumNumbers(root))
