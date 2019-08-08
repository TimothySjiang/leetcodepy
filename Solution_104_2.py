# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        level = 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                children = [node.left, node.right]
                if not any(children): result = level

                for c in children:
                    if c: queue.append(c)

            level += 1

        return result