# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.count = collections.defaultdict(int)
        self.ans = []
        self.search(root)
        return self.ans

    def search(self,root):
        if not root: return '#'
        serial = '{},{},{}'.format(root.val,self.search(root.left),self.search(root.right))
        self.count[serial] += 1
        if self.count[serial] == 2:
            self.ans.append(root)
        return serial