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
        if root:
            queue = [root]
            while queue:
                prev = None
                for i in range(len(queue)):
                    curr = queue.pop(0)
                    if prev:
                        prev.next = curr
                    prev = curr
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            return root