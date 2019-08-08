# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.values())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth[node] == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            if L and R:
                return node
            else:
                return L or R

        return answer(root)