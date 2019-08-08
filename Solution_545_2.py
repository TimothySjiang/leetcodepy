# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.res = []
        self.llevel = collections.defaultdict(int)
        self.rlevel = collections.defaultdict(int)
        self.res.append(root.val)
        self.left(root.left)
        index = len(self.res)
        self.right(root.right)
        return self.res[:index] + self.res[index:][::-1]

    def left(self, root, level=1):
        if not root: return
        if not root.left and not root.right:
            self.res.append(root.val)
            self.llevel[level] = 1
            return
        if self.llevel[level] == 0:
            self.res.append(root.val)
            self.llevel[level] = 1
        self.left(root.left, level + 1)
        self.left(root.right, level + 1)

    def right(self, root, level=1):
        if not root: return
        if not root.left and not root.right:
            self.res.append(root.val)
            self.rlevel[level] = 1
            return
        if self.rlevel[level] == 0:
            self.res.append(root.val)
            self.rlevel[level] = 1
        self.right(root.right, level + 1)
        self.right(root.left, level + 1)
