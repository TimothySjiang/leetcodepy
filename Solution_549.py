# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root,root)
        return self.ans
    def helper(self,node,parent):
        if not node: return 0,0
        li,ld = self.helper(node.left,node)
        ri,rd = self.helper(node.right,node)
        self.ans = max(self.ans,li+rd+1,ld+ri+1)
        if node.val == parent.val + 1:
            return max(li,ri)+1,0
        if node.val == parent.val - 1:
            return 0, max(ld,rd)+1
        return 0,0