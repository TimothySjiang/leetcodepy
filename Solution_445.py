# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        l = self.addTwoNumbersHelp(l1, l2)

        return self.reverse(l)

    def reverse(self, head):
        if not head:
            return head
        pre = None
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr

        return curr

    def addTwoNumbersHelp(self, l1, l2):
        carry = 0
        n = root = ListNode(0)

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next

        return root.next