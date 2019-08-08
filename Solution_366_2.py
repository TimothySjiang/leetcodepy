# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.ans = [[]]
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root: return 0
        if not root.left and not root.right:
            root.depth = 0
            self.ans[0].append(root.val)
            return root.depth + 1
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            root.depth = max(left, right)
            if root.depth >= len(self.ans):
                self.ans.append([root.val])
            else:
                self.ans[root.depth].append(root.val)
            return root.depth + 1