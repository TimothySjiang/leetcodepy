# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            res = TreeNode(v)
            res.left = root
            return res
        queue = [root]
        level = 0
        while level <= d:
            level += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if level == d - 1:
                    temp1 = TreeNode(v)
                    temp1.left = node.left
                    temp2 = TreeNode(v)
                    temp2.right = node.right
                    node.left = temp1
                    node.right = temp2
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root