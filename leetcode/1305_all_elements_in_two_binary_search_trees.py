class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def getAllElements(self, root1, root2):
        result, stack1, stack2 = [], [], []

        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or (stack1 and stack1[-1].value <= stack2[-1].value):
                root1 = stack1.pop()
                result.append(root1.value)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                result.append(root2.value)
                root2 = root2.right

        return result


root1 = Node(0)
root1.left = Node(-10)
root1.right = Node(10)

root2 = Node(5)
root2.left = Node(1)
root2.left.left = Node(0)
root2.left.left.left = Node(-1)
root2.left.right = Node(2)
root2.right = Node(7)

sol = Solution()
print(sol.getAllElements(root1, root2))
