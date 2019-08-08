class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)

        dfs('JFK')
        return route[::-1]