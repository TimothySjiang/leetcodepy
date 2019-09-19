class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges and n <= 2: return [i for i in range(n)]

        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        while len(graph) > 2:
            table = list(graph.keys())
            toDel = []
            for k in table:
                if len(graph[k]) == 1:
                    toDel.append(k)
            for k in toDel:
                graph[graph[k].pop()].remove(k)
                del graph[k]

        return graph.keys()
