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
        dummy = Node(-1, [])
        q = collections.deque([(node, dummy)])
        while q:
            n, parent = q.popleft()
            if n not in visited:
                new_node = Node(n.val, [])
                parent.neighbors.append(new_node)
                for neighbor in n.neighbors:
                    q.append((neighbor, new_node))
                visited[n] = new_node
            else:
                parent.neighbors.append(visited[n])

        return dummy.neighbors[0]