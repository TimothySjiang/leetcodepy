# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res
    def dfs(self,root):
        if not root: return 0
        left = max(0,self.dfs(root.left))
        right = max(0,self.dfs(root.right))
        self.res = max(self.res,left+root.val+right)
        return root.val + max(left,right)