# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(temp)

        return result