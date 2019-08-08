# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list1 = self.sortList(head)
        list2 = self.sortList(mid)

        sorted = self.merge(list1, list2)

        return sorted

    def merge(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = None

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        tmp = head

        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next

        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2

        return head