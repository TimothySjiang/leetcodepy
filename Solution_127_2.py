class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
        if endWord not in wordSet:
            return 0
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)
        level = 1
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                for i in range(len(word)):
                    for j in range(26):
                        if chr(ord('a') + j) == word[i]:
                            continue
                        newword = word[:i] + chr(ord('a') + j) + word[i + 1:]

                        if newword in wordSet and newword not in visited:
                            if newword == endWord:
                                return level + 1
                            visited.add(newword)
                            queue.append(newword)
            level += 1

        return 0