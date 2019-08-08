# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        first = float('inf')
        second = float('inf')
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                if node.val < first:
                    second = first
                    first = node.val
                if first < node.val < second:
                    second = node.val

                queue.append(node.left)
                queue.append(node.right)

        return -1 if second == float('inf') else second

