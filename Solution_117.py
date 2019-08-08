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
            while len(queue) != 0:
                c_queue = []
                prev = None
                while len(queue) != 0:
                    curr = queue.pop(0)
                    if prev:
                        if curr is not prev:
                            prev.next = curr
                    prev = curr
                    if curr.left:
                        c_queue.append(curr.left)
                    if curr.right:
                        c_queue.append(curr.right)
                queue = c_queue
            return root