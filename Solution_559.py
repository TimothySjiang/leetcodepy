"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = [root]
        level = 1
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                children = node.children
                if not any(children): result = level

                for c in children:
                    if c: queue.append(c)

            level += 1

        return result