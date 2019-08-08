# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        n = len(preorder)
        return self.helper(preorder, n)

    def helper(self, preorder, n, lower=float('-inf'), upper=float('inf')):
        if self.idx == n:
            return None
        val = preorder[self.idx]
        if val < lower or val > upper:
            return None
        self.idx += 1
        root = TreeNode(val)
        root.left = self.helper(preorder, n, lower, val)
        root.right = self.helper(preorder, n, val, upper)
        return root