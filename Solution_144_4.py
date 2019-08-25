# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        p = root
        stack = []
        result = []
        while p or stack:
            if p:
                result.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right

        return result