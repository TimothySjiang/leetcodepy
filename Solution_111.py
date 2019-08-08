# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        level = 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if not any([node.left,node.right]): return level
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
