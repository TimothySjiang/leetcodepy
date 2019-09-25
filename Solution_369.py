# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head = self.reverse(head)
        dummy = ListNode(0)
        dummy.next = head
        while head and head.val == 9:
            head.val = 0
            head = head.next
        if head:
            head.val += 1
            return self.reverse(dummy.next)
        else:
            head = ListNode(1)
            head.next = self.reverse(dummy.next)
            return head

    def reverse(self, head):
        pre = None
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr
        return pre