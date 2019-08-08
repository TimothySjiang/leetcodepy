# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.height = self.findDepth(root)
        self.width = (1 << self.height) - 1
        self.dmap = [[""] * self.width for x in range(self.height)]
        self.traverse(root, 1, self.width >> 1)
        return self.dmap
    def findDepth(self, root):
        if not root: return 0
        return 1 + max(self.findDepth(root.left), self.findDepth(root.right))
    def traverse(self, root, depth, offset):
        if not root: return
        self.dmap[depth - 1][offset] = str(root.val)
        gap = 1 + self.width >> depth + 1
        self.traverse(root.left, depth + 1, offset - gap)
        self.traverse(root.right, depth + 1, offset + gap)