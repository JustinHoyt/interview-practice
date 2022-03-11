from typing import List, Optional, DefaultDict
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels: DefaultDict[int, List[int]] = defaultdict(list)

        def dfs(curr: Optional['TreeNode']) -> int:
            if curr is None:
                return 0

            level = max(dfs(curr.left), dfs(curr.right))
            levels[level].append(curr.val)

            return level + 1

        dfs(root)
        return list(levels.values())



def test_happy_path():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    assert [sorted(x) for x in Solution().findLeaves(root)] == [[3,4,5],[2],[1]]


if __name__ == "__main__":
    test_happy_path()

