# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.traversal = []
        self.inOrderDfs(root)
        dummy = head = TreeNode(0)
        for i in range(len(self.traversal)):
            head.right = TreeNode(self.traversal[i])
            head = head.right

        return dummy.right

    def inOrderDfs(self, root):
        if not root: return
        self.inOrderDfs(root.left)
        self.traversal.append(root.val)
        self.inOrderDfs(root.right)