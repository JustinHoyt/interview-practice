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

            curr_sum = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            best_child = max(left, right)

            sum_as_subpath = curr_sum
            sum_as_subpath += best_child if best_child > 0 else 0

            sum_as_pivot = curr_sum
            sum_as_pivot += left if left > 0 else 0
            sum_as_pivot += right if right > 0 else 0

            highest_sum = max(sum_as_pivot, highest_sum)

            return sum_as_subpath

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
