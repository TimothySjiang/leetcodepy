# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.seen = collections.defaultdict(lambda: collections.defaultdict(list))
        ans = []
        self.dfs(root)
        for x in sorted(self.seen):
            res = []
            for y in sorted(self.seen[x]):
                res += sorted(self.seen[x][y])
            ans.append(res)
        return ans

    def dfs(self, root, x=0, y=0):
        if not root: return
        self.seen[x][y].append(root.val)
        self.dfs(root.left, x - 1, y + 1)
        self.dfs(root.right, x + 1, y + 1)