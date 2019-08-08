# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        res = dummy

        while True:
            if not head: break

            start = head

            i = -1
            for i in range(1):
                if head.next:
                    head = head.next
                else:
                    i -= 1
                    break

            while res.next:
                res = res.next

            if i == 0:
                temp = head.next
                head.next = None
                res.next = self.reverse(start)
            else:
                res.next = start
                break

            head = temp

        return dummy.next

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