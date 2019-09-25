"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.recursion(root,res)
        return res
    def recursion(self,root,res):
        if not root: return
        res.append(root.val)
        for child in root.children:
            self.recursion(child,res)