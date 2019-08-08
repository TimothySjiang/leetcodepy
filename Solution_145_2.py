# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        p = root
        stack = []
        result = []
        while p or stack:
            while p:
                result.append(p.val)
                stack.append(p)
                p = p.right
            p = stack.pop()
            p = p.left

        return result[::-1]
