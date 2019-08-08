# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        self.maxLength = 1
        self.dfs(root, None, None)
        return self.maxLength

    def dfs(self, node, parent, length):
        if not node: return
        if parent and node.val == parent.val + 1:
            length = length + 1
            self.maxLength = max(self.maxLength, length)
        else:
            length = 1

        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)