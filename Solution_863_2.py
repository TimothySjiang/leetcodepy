# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.dfs(root)
        queue = [(target, 0)]
        seen = {target}
        while queue:
            for i in range(len(queue)):
                n, d = queue.pop(0)
                if d == K:
                    return [n.val] + [node.val for node, d in queue]

                for nnew in (n.left, n.right, n.par):
                    if nnew and nnew not in seen:
                        seen.add(nnew)
                        queue.append((nnew, d + 1))

        return []

    def dfs(self, node, par=None):
        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)