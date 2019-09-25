# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not self.carry(head):
            return head
        newHead = ListNode(1)
        newHead.next = head
        return newHead

    def carry(self, head):
        if not head: return 1
        carry = self.carry(head.next)
        if not carry: return 0
        val = head.val + 1
        head.val = (val) % 10
        return val // 10



