# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.inorder = []
        self.dfs(root)
        diff = [float('inf')] * (len(self.inorder) - 1)
        for i in range(len(self.inorder) - 1):
            diff[i] = abs(self.inorder[i + 1] - self.inorder[i])
        return min(diff)

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.inorder.append(root.val)
        self.dfs(root.right)