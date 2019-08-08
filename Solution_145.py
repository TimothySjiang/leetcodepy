# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helpPostorder(root, [])

    def helpPostorder(self, root, postorder):
        if not root:
            return postorder

        postorder = self.helpPostorder(root.left, postorder)
        postorder = self.helpPostorder(root.right, postorder)
        postorder.append(root.val)

        return postorder