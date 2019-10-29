class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                queue = [node]
                color[node] = 0
                while queue:
                    for i in range(len(queue)):
                        node = queue.pop(0)
                        for nei in graph[node]:
                            if nei not in color:
                                color[nei] = color[node] ^ 1
                                queue.append(nei)
                            elif color[node] == color[nei]:
                                return False
        return True