# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return False
        queue = [root]
        while queue:
            p = queue.pop(0)
            if p:
                queue.append(p.left)
                queue.append(p.right)
            else:
                break

        if any(queue):
            return False
        else:
            return True