# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        table = set()
        while headA:
            table.add(headA)
            headA = headA.next

        while headB:
            if headB in table:
                return headB
            else:
                headB = headB.next

        return headB