# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = n = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
            else:
                l.next = l2
                l = l.next
                l2 = l2.next
        if l1:
            l.next = l1

        if l2:
            l.next = l2

        return n.next