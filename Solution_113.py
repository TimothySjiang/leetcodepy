# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        self.helpPathsum(root, sum, [])
        return self.result

    def helpPathsum(self, root, target, path):
        if not root:
            return None
        if not root.left and not root.right:
            if target == root.val:
                self.result.append(path + [root.val])
        else:
            self.helpPathsum(root.left, target - root.val, path + [root.val])
            self.helpPathsum(root.right, target - root.val, path + [root.val])