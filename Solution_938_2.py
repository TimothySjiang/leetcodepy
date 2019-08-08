# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        self.dfs(root, L, R)
        return self.total

    def dfs(self, root, L, R):
        if not root: return
        if L <= root.val <= R:
            self.total += root.val
        if L < root.val:
            self.dfs(root.left, L, R)
        if R > root.val:
            self.dfs(root.right, L, R)