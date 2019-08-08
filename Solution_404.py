# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.total = 0
        if not root: return 0
        self.dfs(root, 'right')
        return self.total

    def dfs(self, root, position):
        if not root.left and not root.right and position == 'left':
            self.total += root.val
        if root.left:
            self.dfs(root.left, 'left')
        if root.right:
            self.dfs(root.right, 'right')
