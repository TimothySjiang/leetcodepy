class WordDistance:
    def __init__(self, words: List[str]):
        self.index = collections.defaultdict(list)
        self.res = collections.defaultdict(int)
        for i in range(len(words)):
            self.index[words[i]].append(i)
    def shortest(self, word1: str, word2: str) -> int:
        if (word1 not in self.res) and (word2 not in self.res):
            index1 = self.index[word1]
            index2 = self.index[word2]
            i1 = i2 = 0
            distance  = float('inf')
            while i1 < len(index1) and i2 < len(index2):
                distance = min(distance,abs(index1[i1]-index2[i2]))
                if index1[i1] < index2[i2]:
                    i1 += 1
                else:
                    i2 += 1
            self.res[(word1,word2)] = distance
            return distance
        else:
            return self.res[(word1,word2)] or self.res[(word2,word1)]
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)