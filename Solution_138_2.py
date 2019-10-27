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
        dummy = Node(0, None, None)
        p2 = p3 = dummy
        p1 = head
        dic = {}

        while head:
            p2.next = Node(head.val, None, None)
            dic[head.val] = p2.next
            head = head.next
            p2 = p2.next

        p3 = p3.next
        while p1:
            if p1.random:
                p3.random = dic[p1.random.val]
            p3 = p3.next
            p1 = p1.next

        return dummy.next