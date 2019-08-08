# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right

                if not temp.right:
                    ans.append(root.val)
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    root = root.right
            else:
                ans.append(root.val)
                root = root.right
        return ans