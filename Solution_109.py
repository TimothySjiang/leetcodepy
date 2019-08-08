# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def helpTransfer(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = helpTransfer(nums[:mid])
            root.right = helpTransfer(nums[mid + 1:])

            return root

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = helpTransfer(nums[:mid])
        root.right = helpTransfer(nums[mid + 1:])

        return root