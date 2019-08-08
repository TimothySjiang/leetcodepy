# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        queue = [[root]]
        result = []

        while queue:
            for i in range(len(queue)):
                path = queue.pop(0)
                q = path[-1]

                if not q.left and not q.right:
                    result.append([x.val for x in path])
                    continue

                if q.left:  queue.append(path + [q.left])
                if q.right: queue.append(path + [q.right])

        return ["->".join(str(x)[1:-1].split(', ')) for x in result]