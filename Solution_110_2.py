# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        if not root: return True
        if self.dfs(root) != '#':
            return True
        else:
            return False

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == '#' or right == '#' or abs(left - right) > 1:
            return '#'
        return 1 + max(left, right)