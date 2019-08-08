# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.upper = float('inf')
        self.lower = float('-inf')
        self.helper(root, target)
        return min((self.upper - target, self.upper), (target - self.lower, self.lower))[1]

    def helper(self, root, target):
        if not root: return
        if target < root.val:
            self.upper = root.val
            self.helper(root.left, target)
        if target > root.val:
            self.lower = root.val
            self.helper(root.right, target)
        if target == root.val:
            self.lower = root.val
            self.upper = root.val