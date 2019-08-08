# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        self.ans = 0
        self.dfs(root, root)
        return self.ans + 1

    def dfs(self, root, parent):
        if not root: return 0
        l = self.dfs(root.left, root)
        r = self.dfs(root.right, root)
        if root.val == parent.val + 1:
            self.ans = max(self.ans, max(l, r) + 1)
            return max(l, r) + 1
        return 0