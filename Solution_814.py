# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        prev = TreeNode(0)
        prev.left = root
        self.dfs(root, prev, 'left')

        return prev.left

    def dfs(self, root, prev, pos):
        if root.left:
            self.dfs(root.left, root, 'left')

        if root.right:
            self.dfs(root.right, root, 'right')

        if not root.left and not root.right and not root.val:
            if pos == 'right':
                prev.right = None
            else:
                prev.left = None