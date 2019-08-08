# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        k = self.calculateK(head, k)
        if not k: return head

        start = head
        end = head
        for i in range(k): end = end.next

        while end:
            pre = start
            start = start.next
            end = end.next

        pre.next = None

        startend = start
        while startend.next:
            startend = startend.next

        startend.next = head

        return start

    def calculateK(self, head, k):
        n = 0
        p1 = head
        while p1:
            n += 1
            p1 = p1.next
        k = k % n

        return k
