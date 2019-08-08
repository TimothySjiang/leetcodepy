# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [(root, 'right')]
        total = 0
        while queue:
            n, pos = queue.pop()
            if not n.left and not n.right and pos == 'left':
                total += n.val

            if n.left:
                queue.append((n.left, 'left'))

            if n.right:
                queue.append((n.right, 'right'))

        return total