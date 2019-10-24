class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visites = collections.defaultdict(list)
        for i in range(len(username)):
            visites[username[i]].append((timestamp[i], website[i]))
        count = collections.defaultdict(int)

        for user in visites:
            websites = [x[1] for x in sorted(visites[user])]
            c = set()
            for i in range(len(websites) - 2):
                for j in range(i + 1, len(websites) - 1):
                    for k in range(j + 1, len(websites)):
                        c.add((websites[i], websites[j], websites[k]))
            for sequence in c:
                count[sequence] += 1

        res = ''
        c = 0
        for sequence in count:
            if count[sequence] > c:
                res = sequence
                c = count[sequence]
            elif count[sequence] == c:
                res = min(sequence, res)

        return res