class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]