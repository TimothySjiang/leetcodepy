class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i in range(len(equations)):
            n, d, v = equations[i][0], equations[i][1], values[i]
            graph[n].append((d, v))
            graph[d].append((n, 1 / v))

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
            else:
                tmp = self.dfs(graph, a, b, set())
                if tmp:
                    res.append(tmp)
                else:
                    res.append(-1)

        return res

    def dfs(self, graph, a, b, visited):
        if a == b: return 1
        if a not in visited:
            visited.add(a)
            for p in graph[a]:
                tmp = self.dfs(graph, p[0], b, visited)
                if tmp:
                    return p[1] * tmp
