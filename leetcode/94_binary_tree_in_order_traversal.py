from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order_traversal(root):
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


def post_order_traversal(root):
    nums = []
    stack = deque()
    curr = root
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        nums.append(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return nums

root = TreeNode(5)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
print(in_order_traversal(root))
print(post_order_traversal(root))
