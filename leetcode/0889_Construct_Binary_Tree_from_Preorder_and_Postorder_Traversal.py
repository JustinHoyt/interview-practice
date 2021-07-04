class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        next_node = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:next_node+1], post[:next_node])
        root.right = self.constructFromPrePost(pre[next_node+1:], post[next_node:-1])
        return root

sol = Solution()
print(sol.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))
