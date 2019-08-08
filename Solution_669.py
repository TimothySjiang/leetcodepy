# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def helpTrim(root):
            if not root:
                return None
            if root.val < L:
                return helpTrim(root.right)

            if root.val > R:
                return helpTrim(root.left)

            root.left = helpTrim(root.left)
            root.right = helpTrim(root.right)

            return root

        return helpTrim(root)  