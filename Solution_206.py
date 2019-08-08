# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution_206:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while(head):
            curr = head
            head = head.next
            curr.next = pre
            pre = curr

        return pre