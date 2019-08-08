# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helpPreorder(root, [])

    def helpPreorder(self, root, preorder):
        if not root:
            return preorder

        preorder.append(root.val)
        preorder = self.helpPreorder(root.left, preorder)
        preorder = self.helpPreorder(root.right, preorder)

        return preorder