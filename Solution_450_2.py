# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            val = self.successor(root)
            if val:
                root.val = val
                root.right = self.deleteNode(root.right, val)
            else:
                return root.left
        return root

    def successor(self, root):
        temp = root.right
        while temp and temp.left:
            temp = temp.left
        if temp:
            return temp.val
        return temp