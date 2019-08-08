# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = head
        end = head
        pre = None
        for i in range(n):
            end = end.next
        while end:
            pre = head
            head = head.next
            end = end.next
        if pre:
            pre.next = head.next
            return dummy
        else:
            return dummy.next

