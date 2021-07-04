class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution():
    def countNodes(self, root: TreeNode) -> int:
        temp = root
        count = 1
        is_missing_last = False
        if temp is None:
            return 0
        while temp.right:
            temp = temp.right
            count += 1
        if temp.left:
            count += 1
            is_missing_last = True
        result = 2 ** count - 1
        if is_missing_last:
            result -= 1
        return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
print(count_nodes(root))
