# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        pre = TreeNode(float('-inf'))
        FirstTime = True

        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right

                if not temp.right:
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None

                    if pre.val > root.val and FirstTime:
                        first = pre
                        FirstTime = False
                    if pre.val > root.val and not FirstTime:
                        second = root
                    pre = root

                    root = root.right
            else:

                if pre.val > root.val and FirstTime:
                    first = pre
                    FirstTime = False
                if pre.val > root.val and not FirstTime:
                    second = root
                pre = root

                root = root.right

        if first and second:
            temp = first.val
            first.val = second.val
            second.val = temp