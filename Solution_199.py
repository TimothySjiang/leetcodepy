# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            temp = []
            for i in range(len(queue)):
                current = queue.pop(0)
                temp.append(current.val)
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
            result.append(temp[-1])

        return result