# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        root.pos = 1
        queue = [root]
        res = 0
        while queue:
            min_pos = queue[0].pos
            max_pos = queue[-1].pos
            res = max(res,max_pos-min_pos+1)
            for i in range(len(queue)):
                p = queue.pop(0)
                if p.left:
                    p.left.pos = p.pos*2-1
                    queue.append(p.left)
                if p.right:
                    p.right.pos = p.pos*2
                    queue.append(p.right)
        return res