# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        return self.helpGenerateTrees(1, n)

    def helpGenerateTrees(self, start, end):
        if start > end: return [None]
        res = []
        for i in range(start, end + 1):
            left = self.helpGenerateTrees(start, i - 1)
            right = self.helpGenerateTrees(i + 1, end)
            for l in left:
                for r in right:
                    temp = TreeNode(i)
                    temp.left = l
                    temp.right = r
                    res.append(temp)
        return res