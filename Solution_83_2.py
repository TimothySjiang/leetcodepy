# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        seen = set()
        pre = None
        dummy = head
        while head:
            if head.val not in seen:
                seen.add(head.val)
                if pre:
                    pre.next = head
                pre = head
                head = head.next
            else:
                head = head.next
        if pre:
            pre.next = head

        return dummy
