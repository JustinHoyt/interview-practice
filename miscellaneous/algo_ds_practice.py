from heapq import heappush, heappop
from collections import deque
def heap_practice(nums):
    heap = []

    # min heap
    for num in nums:
        heappush(heap, num)

    while heap:
        print(heappop(heap))

    print()

    # max heap
    for num in nums:
        heappush(heap, -num)

    while heap:
        print(-heappop(heap))

# heap_practice([2,7,4,9,33,6,87])


def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1

# print(binary_search([1,2,3,4,7,9,22,54,89], 7))

def find_closest(nums, target):
    left = 0
    right = len(nums)-1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid
        else:
            right = mid

    if abs(target - nums[left]) < abs(target - nums[right]):
        return left
    else:
        return right

# print(find_closest([1,2,3,4,7,9,22,54,89], 66))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_mode(root):
    best_count = 0
    mode = 0

    def in_order(node):
        nonlocal best_count
        nonlocal mode

        if not node:
            return 0, 0


        left_count, left_num = in_order(node.left)

        curr_count = 1
        if node.val == left_num:
            curr_count += left_count

        in_order(node.right)

        if curr_count > best_count:
            best_count, mode = curr_count, node.val

        return curr_count, node.val

    in_order(root)
    return mode

tree = TreeNode(200)
tree.left = TreeNode(100)
tree.left.right = TreeNode(150)
tree.left.right.right = TreeNode(170)
tree.left.right.right.left = TreeNode(170)
tree.left.right.right.left.left = TreeNode(160)
tree.left.right.right.left.left.left = TreeNode(160)
tree.left.right.right.left.left.left.left = TreeNode(160)
tree.left.left = TreeNode(90)
tree.left.left.left = TreeNode(80)
tree.left.left.left.left = TreeNode(70)

# print(find_mode(tree))

def tree_bfs_track_level(root):
    queue = deque()
    max_level = 0

    queue.append((root, 1))
    while queue:
        node, level = queue.popleft()
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

        max_level = max(max_level, level)

    return max_level

print(tree_bfs_track_level(tree))

