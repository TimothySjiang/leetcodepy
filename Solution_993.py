# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.seen = []
        self.x = x
        self.y = y
        self.dfs(root, None, -1)
        return self.seen[0].par != self.seen[1].par and self.seen[0].depth == self.seen[1].depth

    def dfs(self, root, par, depth):
        if not root: return None
        if len(self.seen) == 2:
            return
        if root.val == self.x or root.val == self.y:
            self.seen.append(root)

        root.par = par
        root.depth = depth + 1

        self.dfs(root.left, root, root.depth)
        self.dfs(root.right, root, root.depth)