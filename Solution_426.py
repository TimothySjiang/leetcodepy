"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        self.first,self.last = None,None
        self.inOrderDfs(root)
        self.last.right = self.first
        self.first.left = self.last

        return self.first


    def inOrderDfs(self,root):
        if not root: return
        self.inOrderDfs(root.left)
        if self.last:
            self.last.right = root
            root.left = self.last
        else:
            self.first = root
        self.last = root
        self.inOrderDfs(root.right)