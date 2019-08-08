# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.res = [root.val]
        if not root.left and not root.right: return self.res
        self.leftBoundary(root.left)
        self.leaf(root)
        self.rightBoundary(root.right)
        return self.res

    def leftBoundary(self, root):
        if not root or (not root.left and not root.right):
            return
        self.res.append(root.val)
        if root.left:
            self.leftBoundary(root.left)
        else:
            self.leftBoundary(root.right)

    def rightBoundary(self, root):
        if not root or (not root.left and not root.right):
            return
        if root.right:
            self.rightBoundary(root.right)
        else:
            self.rightBoundary(root.left)
        self.res.append(root.val)

    def leaf(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res.append(root.val)
            return
        self.leaf(root.left)
        self.leaf(root.right)