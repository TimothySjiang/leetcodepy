class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        distance = len(words)
        index1 = index2 = -1
        if word1 != word2:
            for i in range(len(words)):
                if words[i] == word1:
                    index1 = i
                    if index1 != -1 and index2 != -1:
                        distance = min(distance, abs(index1 - index2))
                if words[i] == word2:
                    index2 = i
                    if index1 != -1 and index2 != -1:
                        distance = min(distance, abs(index1 - index2))
        else:
            index = len(words)
            for i in range(len(words)):
                if words[i] == word1:
                    distance = min(distance, abs(index - i))
                    index = i

        return distance