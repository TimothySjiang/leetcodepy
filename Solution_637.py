# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            n = len(queue)
            total = 0
            for i in range(n):
                p = queue.pop(0)

                total += p.val
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)

            res += [total / n]

        return res