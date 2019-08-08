# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root.left and not root.right:
            return root.val, root.val

        if root.left and root.right:
            submax1, submin1 = self.dfs(root.left)
            submax2, submin2 = self.dfs(root.right)

            submax = max(submax1, submax2)
            submin = min(submin1, submin2)
        else:
            if root.left:
                submax, submin = self.dfs(root.left)
            if root.right:
                submax, submin = self.dfs(root.right)

        self.ans = max([abs(root.val - submax), abs(root.val - submin), self.ans])

        return max(submax, root.val), min(submin, root.val)