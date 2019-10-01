class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
    	if not root.left or not root.right:
    	    return False
    	return self.areEqual(root.left, root.right)


    def areEqual(self, node1, node2):
        # Code here
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        left = self.areEqual(node1.left, node2.right)
        right = self.areEqual(node1.right, node2.left)

        return node1.val == node2.val and left and right
