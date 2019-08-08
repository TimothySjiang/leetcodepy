# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))

    def dp(self, root):
        if not root: return 0, 0
        left = self.dp(root.left)
        right = self.dp(root.right)
        now = root.val + left[1] + right[1]
        later = max(left) + max(right)
        return now, later