"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dummy = Node(-1, [])
        visited = {}
        self.recursion(dummy, node, visited)
        return dummy.neighbors[0]

    def recursion(self, par, child, visited):
        if child not in visited:
            newChild = Node(child.val, [])
            par.neighbors.append(newChild)
            visited[child] = newChild
            for c in child.neighbors:
                self.recursion(newChild, c, visited)
        else:
            par.neighbors.append(visited[child])