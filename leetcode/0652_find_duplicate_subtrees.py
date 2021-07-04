import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node: return "#"
            # serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            serial = f'{node.val},{collect(node.left)},{collect(node.right)}'
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


sol = Solution()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.right = TreeNode(3)
tree.right.left = TreeNode(2)
tree.right.left.left = TreeNode(4)
tree.right.right = TreeNode(4)

for ele in sol.findDuplicateSubtrees(tree):
    print(ele)
# print(sol.findDuplicateSubtrees(tree))
