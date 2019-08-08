# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.c = collections.Counter()
        self.dfs(root)
        max_freq = max(self.c.values())

        return [k for k in self.c if self.c[k] == max_freq]

    def dfs(self, root):
        if not root:
            return
        self.c[root.val] += 1
        self.dfs(root.left)
        self.dfs(root.right)
