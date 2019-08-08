# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.Max = 0
        self.helper(root)

        return self.Max

    def helper(self,root):
        if(root == None):
            return
        left = root.left
        right = root.right
        self.Max=max(self.Max,self.depth(left)+self.depth(right))

        self.helper(left)
        self.helper(right)

    def depth(self,root):
        if(root == None):
            return 0
        left = root.left
        right = root.right
        if (left == None and right == None):
            return 1
        if(left == None):
            return 1 + self.depth(right)
        if(right == None):
            return 1 + self.depth(left)
        else:
            return 1 + max(self.depth(left),self.depth(right))