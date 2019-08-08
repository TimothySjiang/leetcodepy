# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        r = n = ListNode(0)

        loop = True
        while loop:
            loop = False
            toCompare = []
            MIN = float("inf")
            this = float('inf')
            for i, head in enumerate(lists):
                if head:
                    loop = True
                    if MIN <= head.val:
                        continue
                    else:
                        MIN = head.val
                        this = i
            if loop:
                lists[this] = lists[this].next
                n.next = ListNode(MIN)
                n = n.next

        return r.next
