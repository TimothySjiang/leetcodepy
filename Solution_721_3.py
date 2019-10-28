class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        graph = collections.defaultdict(list)
        for account in accounts:
            graph[account[1]].append(account[1])
            for i in range(1, len(account)):
                for j in range(i + 1, len(account)):
                    graph[account[i]].append(account[j])
                    graph[account[j]].append(account[i])
                emailToName[account[i]] = account[0]

        res = []
        seen = set()
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for e in graph[node]:
                        if e not in seen:
                            seen.add(e)
                            stack.append(e)
                res.append([emailToName[email]] + sorted(component))
        return res