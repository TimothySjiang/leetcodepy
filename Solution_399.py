class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))
        res = []
        for a, b in queries:
            if a not in graph.keys() or b not in graph.keys():
                res.append(-1)
            else:
                t = self.dfs(graph, a, b, set())
                if t:
                    res.append(t)
                else:
                    res.append(-1)
        return res

    def dfs(self, graph, a, b, seen):
        if a == b:
            return 1
        if a not in seen:
            seen.add(a)
            for p in graph[a]:
                t = self.dfs(graph, p[0], b, seen)
                if t:
                    return p[1] * t
