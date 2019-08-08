class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        all_combo = collections.defaultdict(list)
        L = len(beginWord)
        for w in wordList:
            for i in range(L):
                all_combo[w[:i] + '*' + w[i + 1:]].append(w)

        visited = {}
        queue = [[(beginWord, 1)]]
        result = []
        R = False
        level = 1
        while queue and not R and level < len(wordList):
            for i in range(len(queue)):
                path = queue.pop(0)
                node, level = path[-1]
                for i in range(L):
                    nextStep = node[:i] + '*' + node[i + 1:]
                    for word in all_combo[nextStep]:
                        if word == endWord:
                            result.append([x[0] for x in (path + [(word, level + 1)])])
                            R = True
                        else:
                            if word not in visited.keys() or level == visited[word] - 1:
                                queue.append(path + [(word, level + 1)])
                                visited[word] = level + 1

        return result