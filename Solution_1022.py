# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root: return 0
        self.total = 0
        self.dfs(root, 0)

        return self.total

    def dfs(self, root, par):
        if not root.left and not root.right:
            self.total += par * 2 + root.val
        if root.left:
            self.dfs(root.left, par * 2 + root.val)
        if root.right:
            self.dfs(root.right, par * 2 + root.val)