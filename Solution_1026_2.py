# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        return self.dfs(root, high=root.val, low=root.val)

    def dfs(self, root, high, low):
        if not root: return high - low
        high = max(high, root.val)
        low = min(low, root.val)
        return max(self.dfs(root.left, high, low), self.dfs(root.right, high, low))