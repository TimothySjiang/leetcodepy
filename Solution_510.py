"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            return temp
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent