# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.res = {}
        self.ans = False
        self.inorder(root, k)
        return self.ans

    def inorder(self, root, k):
        if not root: return
        self.inorder(root.left, k)
        if root.val not in self.res:
            self.res[k - root.val] = root.val
        else:
            self.ans = True
        self.inorder(root.right, k)