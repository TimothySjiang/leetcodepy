# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        while n + 1:
            first = first.next
            n -= 1

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next