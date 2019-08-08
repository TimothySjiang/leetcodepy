# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            max_row = []
            for i in range(len(queue)):
                p = queue.pop(0)

                max_row.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)

            res.append(max(max_row))

        return res
