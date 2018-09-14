from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    nums = []
    stack = deque()
    curr = root
    while len(stack) > 0 or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        nums.append(curr.val)
        curr = curr.right
    return nums

root = TreeNode(5)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
print(inorderTraversal(root))
