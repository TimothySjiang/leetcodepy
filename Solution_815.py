#TLE
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        ByStation = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for station in route:
                ByStation[station].append(i)

        queue = [S]
        level = 0
        visited = set()
        visited.add(S)
        while queue:
            for i in range(len(queue)):
                s = queue.pop(0)
                if s == T:
                    return level
                for bus in ByStation[s]:
                    for s in routes[bus]:
                        if s not in visited:
                            visited.add(s)
                            queue.append(s)

            level += 1

        return -1