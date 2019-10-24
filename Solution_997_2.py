class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for edge in trust:
            graph[edge[0]].add(edge[1])
        candidate = 0
        for i in range(1,N+1):
            if not graph[i]:
                if candidate:
                    return -1
                candidate = i
        for i in range(1,N+1):
            if i != candidate:
                if candidate not in graph[i]:
                    return -1
        return candidate