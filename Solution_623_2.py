# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            temp = TreeNode(v)
            temp.left = root
            return temp
        queue = [root]
        depth = 0
        while queue and depth != d-1:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if depth == d-1:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    if left: node.left.left = left
                    if right: node.right.right = right
                else:
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
        return root