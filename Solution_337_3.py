# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.dp(root)

    def dp(self, root):
        if not root: return 0
        if root.ans != '#':
            return root.ans
        if root.left and root.right:
            num1 = root.val + self.dp(root.left.left) + self.dp(root.left.right) + self.dp(root.right.left) + self.dp(
                root.right.right)
            num2 = self.dp(root.left) + self.dp(root.right)
            root.ans = max(num1, num2)
        elif root.left:
            num1 = root.val + self.dp(root.left.left) + self.dp(root.left.right)
            num2 = self.dp(root.left)
            root.ans = max(num1, num2)
        elif root.right:
            num1 = root.val + self.dp(root.right.left) + self.dp(root.right.right)
            num2 = self.dp(root.right)
            root.ans = max(num1, num2)
        else:
            root.ans = root.val
        return root.ans

    def dfs(self, root):
        if not root: return
        root.ans = '#'
        self.dfs(root.left)
        self.dfs(root.right)