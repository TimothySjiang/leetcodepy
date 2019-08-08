# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not (root): return []

        res, MIN, MAX = [], 0, 0
        table = collections.defaultdict(list)
        queue = [(root, 0)]

        while queue:
            # order matters
            node, index = queue.pop(0)
            table[index].append(node.val)

            # left comes first.
            if node.left:
                queue.append((node.left, index - 1))
            if node.right:
                queue.append((node.right, index + 1))

        for i in sorted(table.keys()):
            res.append(table[i])

        return res