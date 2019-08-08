# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        p = root
        stack = []
        ans = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans.append(p.val)
            p = p.right
        return ans
