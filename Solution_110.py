# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left = root.left
        right = root.right

        if abs(self.depth(left) - self.depth(right)) > 1:
            return False

        return self.isBalanced(left) and self.isBalanced(right)

    def depth(self, root):
        if root == None:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))