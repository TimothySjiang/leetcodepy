"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        if root.left:
            if root.right:
                root.left.next = root.right
            elif root.next:
                if root.next.left:
                    root.left.next = root.next.left
                else:
                    root.left.next = root.next.right

        if root.right:
            if root.next:
                if root.next.left:
                    root.right.next = root.next.left
                else:
                    root.right.next = root.next.right

        self.connect(root.left)
        self.connect(root.right)

        return root