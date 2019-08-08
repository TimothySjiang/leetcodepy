"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        ans = []
        while queue:
            res = []
            for i in range(len(queue)):
                p = queue.pop(0)
                res.append(p.val)
                for child in p.children:
                    queue.append(child)
            ans.append(res)
        return ans