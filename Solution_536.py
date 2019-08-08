# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        ix = s.find('(')
        if ix < 0:
            return TreeNode(int(s)) if s else None

        stack = ['(']
        for i in range(ix + 1, len(s)):
            if s[i] == '(': stack.append('(')
            if s[i] == ')': stack.pop()
            if not stack:
                jx = i
                break

        root = TreeNode(int(s[:ix]))
        root.left = self.str2tree(s[ix + 1:jx])
        root.right = self.str2tree(s[jx + 2:-1])
        return root