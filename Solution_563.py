# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    def dfs(self,root):
        if not root:return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.ans += abs(l-r)
        return l+r+root.val