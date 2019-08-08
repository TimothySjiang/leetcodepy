# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans = 0
        self.k = k
        self.helpInorder(root)
        return self.ans
    def helpInorder(self,root):
        if not root: return
        self.helpInorder(root.left)
        self.k-=1
        if not self.k:
            self.ans = root.val
            return
        self.helpInorder(root.right)