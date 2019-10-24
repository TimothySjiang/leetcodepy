class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            root1, root2 = find(a), find(b)
            if root1 != root2:
                root[root2] = root1
            return

        root = {city: city for city in range(1, N + 1)}

        connections_asc = sorted(connections, key=lambda x: x[2])

        total = 0
        count = N
        for city1, city2, cost in connections_asc:
            if find(city1) != find(city2):
                union(city1, city2)
                count -= 1
                total += cost
        if count == 1:
            return total
        else:
            return -1