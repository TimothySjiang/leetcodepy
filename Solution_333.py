# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return float('inf'), float('-inf'), 0, True
        minleft, maxleft, numleft, bstLeft = self.dfs(root.left)
        minright, maxright, numright, bstRight = self.dfs(root.right)
        if bstLeft and bstRight:
            if maxleft < root.val < minright:
                self.ans = max(self.ans, numleft + numright + 1)
                return min(minleft, root.val), max(maxright, root.val), numleft + numright + 1, True
        return 0, 0, 0, False