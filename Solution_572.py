# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)

    def equals(self, x, y):
        if (x == None and y == None):
            return True
        if (x == None or y == None):
            return False
        return x.val == y.val and self.equals(x.left, y.left) and self.equals(x.right, y.right)

    def traverse(self, s, t):
        return s != None and (self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))