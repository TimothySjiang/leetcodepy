# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        results = []
        self.dfs(root, None, to_delete, results, 'left')
        return results

    def dfs(self, root, par, to_delete, results, pos):
        if not root: return
        if root.val in to_delete:
            if not par:
                to_delete.remove(root.val)
                self.dfs(root.left, par, to_delete, results, 'left')
                self.dfs(root.right, par, to_delete, results, 'right')
            else:
                if pos == 'left':
                    par.left = None
                else:
                    par.right = None
                self.dfs(root.left, None, to_delete, results, 'left')
                self.dfs(root.right, None, to_delete, results, 'right')
        else:
            if not par:
                results.append(root)
            self.dfs(root.left, root, to_delete, results, 'left')
            self.dfs(root.right, root, to_delete, results, 'right')