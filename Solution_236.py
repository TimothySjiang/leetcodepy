# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helpLCA(root, p, q)
        return self.ans

    def helpLCA(self, root, p, q):
        if not root:
            return False

        left = self.helpLCA(root.left, p, q)
        right = self.helpLCA(root.right, p, q)

        mid = root.val == p.val or root.val == q.val

        if mid + right + left >= 2:
            self.ans = root

        return mid or left or right