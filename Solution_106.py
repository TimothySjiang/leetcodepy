# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        rightPreorder = postorder[::-1]
        return self.helpBuildTree(inorder, rightPreorder)

    def helpBuildTree(self, inorder, rightPreorder):
        if not inorder:
            return None
        else:
            index = inorder.index(rightPreorder.pop(0))
            root = TreeNode(inorder[index])
            root.right = self.helpBuildTree(inorder[index + 1:], rightPreorder)
            root.left = self.helpBuildTree(inorder[:index], rightPreorder)

        return root
