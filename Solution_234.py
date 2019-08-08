# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        p1 = head.next
        p2 = head
        pre = head
        while p2.next and p2.next.next:
            p2 = p2.next.next
            curr = p1
            p1 = p1.next
            curr.next = pre
            pre = curr

        if not p2.next:
            pre = pre.next

        while p1 and pre:
            if p1.val != pre.val:
                return False
            p1 = p1.next
            pre = pre.next

        return True



