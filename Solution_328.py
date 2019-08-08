# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        po = ListNode(0)
        pe = ListNode(0)
        dummyo = po
        dummye = pe

        i = 1
        while head:
            if i % 2:
                po.next = ListNode(head.val)
                po = po.next
            else:
                pe.next = ListNode(head.val)
                pe = pe.next
            head = head.next
            i += 1

        po.next = dummye.next

        return dummyo.next

