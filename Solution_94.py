# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal_re(root, [])

    def inorderTraversal_re(self, root, inorder):
        if not root:
            return inorder
        inorder = self.inorderTraversal_re(root.left, inorder)
        inorder.append(root.val)
        inorder = self.inorderTraversal_re(root.right, inorder)
        return inorder
