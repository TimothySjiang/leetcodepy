# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.leaves = []

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        self.tree_height(root)
        return self.leaves

    def tree_height(self, root):
        if root == None:
            return -1
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        height = 1 + max(left_height, right_height)
        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)
        return height