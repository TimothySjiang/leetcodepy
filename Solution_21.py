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
        while l1 or l2:
            if l1:
                if l2:
                    if l1.val < l2.val:
                        v = l1.val
                        l1 = l1.next
                    else:
                        v = l2.val
                        l2 = l2.next
                    l.next = ListNode(v)
                    l = l.next
                else:
                    l.next = l1
                    break
            else:
                l.next = l2
                break
        return (n.next)
