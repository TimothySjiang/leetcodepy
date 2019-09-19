class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges and n <= 2: return [i for i in range(n)]
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        leaves = []
        for k in graph:
            if len(graph[k]) <= 1:
                leaves.append(k)

        while n > 2:
            newLeaves = []
            for leaf in leaves:
                neighbor = next(iter(graph[leaf]))
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
                n -= 1
            leaves = newLeaves

        return leaves

