# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import ListNode
class Solution_203:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        fakehead = ListNode(0)
        curr = head
        fakehead.next = head
        prev = fakehead
        while(curr != None):
            if(curr.val == val ):
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return fakehead.next
