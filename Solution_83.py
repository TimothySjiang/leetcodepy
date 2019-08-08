# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        t = result = ListNode(0)
        while head:
            if head.val not in s:
                s.add(head.val)
                result.next = ListNode(head.val)
                result = result.next

            head = head.next

        return t.next