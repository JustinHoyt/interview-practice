class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def maxPathSum(self, root):
        highest_sum = float('-INF')

        def dfs(node):
            nonlocal highest_sum

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            best_child = max(left, right)

            sum_with_best_child = node.val + best_child

            sum_with_both_children = node.val + left + right

            highest_sum = max(sum_with_both_children, highest_sum)

            if sum_with_best_child < 0:
                return 0
            return sum_with_best_child

        dfs(root)
        return highest_sum


sol = Solution()

# root = Node(-10)
# root.left = Node(9)
# root.right = Node(20)
# root.right.left = Node(15)
# root.right.right = Node(7)

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.left.left = Node(7)
root.right.left.right = Node(2)
root.right.right.right = Node(1)

# [5,4,8,11,null,13,4,7,2,null,null,null,1]

print(sol.maxPathSum(root))
