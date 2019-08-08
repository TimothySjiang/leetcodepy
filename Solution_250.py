# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.helpDfs(root)
        return self.count

    def helpDfs(self, root):
        if not root:
            return (None, True)
        if not root.left and not root.right:
            self.count += 1
            return (root.val, True)

        left, unil = self.helpDfs(root.left)
        right, unir = self.helpDfs(root.right)

        uni = False
        if unil and unir:
            if left and right:
                uni = left == right == root.val
            else:
                if left: uni = left == root.val
                if right: uni = right == root.val

        if uni:
            self.count += 1

        return (root.val, uni)