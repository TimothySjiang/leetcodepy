# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = "~"
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, path):
        if root:
            path.append(chr(root.val + ord('a')))
            if not root.left and not root.right:
                self.ans = min(self.ans, ''.join(path[::-1]))

            self.dfs(root.left, path)
            self.dfs(root.right, path)
            path.pop()