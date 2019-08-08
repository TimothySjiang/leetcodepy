# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        visited = {}

        def helpRob(root, path):
            if root is None: return 0
            if path not in visited:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:  ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right

                passup = helpRob(left, path + 'l') + helpRob(right, path + 'r')
                grabit = root.val + helpRob(ll, path + 'll') + helpRob(lr, path + 'lr') + helpRob(rl,
                                                                                                  path + 'rl') + helpRob(
                    rr, path + 'rr')
                visited[path] = max(passup, grabit)

            return visited[path]

        return helpRob(root, '')