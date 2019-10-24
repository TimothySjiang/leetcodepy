"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = head
        while head:
            if head.child:
                tmp = head.next
                head.child.prev = head
                head.next = self.flatten(head.child)
                head.child = None
                while head.next:
                    head = head.next
                if tmp:
                    head.next = tmp
                    tmp.prev = head
            head = head.next
        return dummy