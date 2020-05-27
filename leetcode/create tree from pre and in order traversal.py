# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        # find the root of your subtree
        root = TreeNode(preorder.pop(0))

        # find the idx of the root val in the in-order traversal
        inorder_root_index = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:inorder_root_index])
        root.right = self.buildTree(preorder, inorder[inorder_root_index+1:])

        return root