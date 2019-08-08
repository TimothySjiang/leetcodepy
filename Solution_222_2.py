# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        leftD = self.getDepth(root.left)
        rightD = self.getDepth(root.right)

        if leftD == rightD:
            return pow(2, leftD) + self.countNodes(root.right)
        else:
            return pow(2, rightD) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root: return 0
        return 1 + self.getDepth(root.left)

