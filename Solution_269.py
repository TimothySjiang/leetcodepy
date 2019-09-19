class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(set)
        Set = set()
        queue = []
        res = ''

        for word in words:
            for c in word:
                Set.add(c)

        for i in range(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            for j in range(0, minLen):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i + 1][j]].add(words[i][j])
                    break
                if j == minLen - 1 and len(words[i]) > len(words[i + 1]):
                    return ''
        for key in Set:
            if not graph[key]:
                queue.append(key)
                res += key

        while queue:
            c = queue.pop(0)
            for key in graph:
                if c in graph[key]:
                    graph[key].remove(c)
                    if not graph[key]:
                        queue.append(key)
                        res += key

        return res if len(res) == len(Set) else ''
