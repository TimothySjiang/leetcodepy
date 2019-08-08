# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafSequence1 = self.dfs(root1, [])
        leafSequence2 = self.dfs(root2, [])

        return leafSequence1 == leafSequence2

    def dfs(self, root, ans):
        if not root.left and not root.right:
            ans.append(root.val)
            return ans
        if root.left:
            ans = self.dfs(root.left, ans)
        if root.right:
            ans = self.dfs(root.right, ans)

        return ans