"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = p1 = p2 = Node(0, None, None)
        p3 = head
        store = {}
        while head:
            p1.next = Node(head.val, None, None)
            head = head.next
            p1 = p1.next
            store[p1.val] = p1

        while p3:
            if p3.random:
                i = p3.random.val
                p2.next.random = store[i]
                p2 = p2.next
                p3 = p3.next
            else:
                p2 = p2.next
                p3 = p3.next

        return dummy.next