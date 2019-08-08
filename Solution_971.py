# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.flipped = []
        self.dfs(root, voyage)
        return self.flipped

    def dfs(self, root, voyage):
        if root:
            if root.val != voyage[self.i]:
                self.flipped = [-1]
                return
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                self.flipped.append(root.val)
                self.dfs(root.right, voyage)
                self.dfs(root.left, voyage)
            else:
                self.dfs(root.left, voyage)
                self.dfs(root.right, voyage)