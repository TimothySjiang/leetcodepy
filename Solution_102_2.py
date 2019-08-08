# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def help_level(root, level, ans):
            if root:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(root.val)
                if root.left: help_level(root.left, level + 1, ans)
                if root.right: help_level(root.right, level + 1, ans)

        ans = []
        help_level(root, 0, ans)
        return ans