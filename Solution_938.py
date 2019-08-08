# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        total = 0
        queue = [root]
        while queue:
            p = queue.pop()
            if not p:
                continue
            if L <= p.val <= R:
                total += p.val
            if L < p.val:
                queue.append(p.left)
            if R > p.val:
                queue.append(p.right)

        return total