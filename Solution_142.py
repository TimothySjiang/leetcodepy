# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        p1 = head
        p2 = head
        while True:
            if not p2.next or not p2.next.next:
                return None
            else:
                p1 = p1.next
                p2 = p2.next.next
                if p1 == p2:
                    break

        p3 = head
        while p3 != p2:
            p2 = p2.next
            p3 = p3.next

        return p3