"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return
        self.ans.append(root.val)
        for child in root.children:
            self.dfs(child)