# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.flag = root.val
        return self.dfs(root)

    def dfs(self, root):
        if not root: return True
        if root.val != self.flag:
            return False
        return self.dfs(root.left) and self.dfs(root.right)