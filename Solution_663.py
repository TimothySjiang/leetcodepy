# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        if not root: return False
        self.target = []
        total = self.dfs(root)
        self.target.pop()
        return total / 2 in self.target

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.target.append(left + right + root.val)
        return left + right + root.val