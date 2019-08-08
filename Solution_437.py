# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        res = self.dfs(root,sum)
        res += self.pathSum(root.left,sum)
        res += self.pathSum(root.right,sum)
        return res
    def dfs(self,root,val):
        if not root: return 0
        res =  (root.val == val)
        res += self.dfs(root.left,val-root.val)
        res += self.dfs(root.right,val-root.val)
        return res