# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.c = collections.defaultdict(int)
        self.dfs(root)
        max_value = max(self.c.values())
        res = []
        for k in self.c:
            if self.c[k] == max_value:
                res.append(k)

        return res

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        total = left + right + root.val
        self.c[total] += 1
        return total