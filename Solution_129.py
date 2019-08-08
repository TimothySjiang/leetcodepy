# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.help_sum(root, 0)
        return self.res

    def help_sum(self, root, par_sum):
        if not root.left and not root.right:
            self.res += par_sum * 10 + root.val
        if root.left:
            self.help_sum(root.left, par_sum * 10 + root.val)
        if root.right:
            self.help_sum(root.right, par_sum * 10 + root.val)

