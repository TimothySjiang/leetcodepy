# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p1 = head
        pre = None
        for i in range(m - 1):
            pre = p1
            p1 = p1.next
        p2 = p1
        for i in range(n - m):
            p2 = p2.next
        p3 = p2.next
        p2.next = None

        mid = self.reverse(p1)
        if not pre:
            head = mid
        else:
            pre.next = mid

        while mid.next:
            mid = mid.next

        mid.next = p3

        return head

    def reverse(self, head):
        if not head:
            return None
        pre = None
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr

        return curr