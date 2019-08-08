# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helpPaths(root, path):
            if not root:
                return None

            path += str(root.val)

            if not root.left and not root.right:
                paths.append(path)
            else:
                path += "->"
                helpPaths(root.left, path)
                helpPaths(root.right, path)

        paths = []
        helpPaths(root, '')
        return paths