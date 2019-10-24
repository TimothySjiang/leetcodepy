class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for city1, city2, cost in connections:
            graph[city1].append((cost, city2))
            graph[city2].append((cost, city1))

        queue = [(0, 1)]
        visited = set()
        total = 0
        while queue and len(visited) < N:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for neighbor in graph[city]:
                    heapq.heappush(queue, neighbor)
        if len(visited) == N:
            return total
        else:
            return -1
