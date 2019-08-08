from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo = defaultdict(list)

        for w in wordList:
            for i in range(L):
                all_combo[w[:i] + "*" + w[i + 1:]].append(w)

        visited = set()
        queue = [(beginWord, 1)]

        while queue:
            current, level = queue.pop(0)
            for i in range(L):
                immediateWord = current[:i] + '*' + current[i + 1:]
                for word in all_combo[immediateWord]:
                    if word == endWord:
                        return level + 1
                    else:
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, level + 1))
                all_combo[immediateWord] = []

        return 0