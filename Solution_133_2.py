"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        dummy = Node(-1,[])
        queue = [(dummy,node)]
        while queue:
            parent,child  = queue.pop(0)
            if child not in visited:
                newChild = Node(child.val,[])
                parent.neighbors.append(newChild)
                for c in child.neighbors:
                    queue.append((newChild,c))
                visited[child] = newChild
            else:
                parent.neighbors.append(visited[child])
        return dummy.neighbors[0]