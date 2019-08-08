# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            root = TreeNode(t1.val)
            root.left = t1.left
            root.right = t1.right
        elif t2:
            root = TreeNode(t2.val)
            root.left = t2.left
            root.right = t2.right

        return root
