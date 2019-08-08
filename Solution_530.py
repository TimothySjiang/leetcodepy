# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = []
        self.inOrderDfs(root)
        min_diff = float('inf')
        for i in range(len(self.res) - 1):
            diff = self.res[i + 1] - self.res[i]
            min_diff = min(diff, min_diff)
        return min_diff

    def inOrderDfs(self, root):
        if not root:
            return
        self.inOrderDfs(root.left)
        self.res.append(root.val)
        self.inOrderDfs(root.right)