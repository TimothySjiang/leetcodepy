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
        current = root
        mostleft = current.left
        while mostleft:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
                current = current.next
            else:
                current = mostleft
                mostleft = current.left

        return root