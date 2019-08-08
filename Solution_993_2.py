# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root, x, y):
        parent = {}
        depth = {}
        self.dfs(root, depth, parent)
        return depth[x] == depth[y] and parent[x] != parent[y]

    def dfs(self, node, depth, parent, par=None):
        if node:
            depth[node.val] = 1 + depth[par.val] if par else 0
            parent[node.val] = par
            self.dfs(node.left, depth, parent, node)
            self.dfs(node.right, depth, parent, node)