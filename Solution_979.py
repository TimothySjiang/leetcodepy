# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    def dfs(self,root):
        if not root: return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans += abs(l) + abs(r)
        return l+r+root.val - 1