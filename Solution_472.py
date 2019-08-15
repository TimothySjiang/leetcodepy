class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if not words: return []
        results = []
        for i in range(len(words)):
            wlist = words[:i] + words[i + 1:]
            if self.dfs(wlist, words[i]):
                results.append(words[i])
        return results

    def dfs(self, wlist, target):
        if not target: return True
        for i in range(len(wlist)):
            if wlist[i] == target[:len(wlist[i])]:
                if self.dfs(wlist, target[len(wlist[i]):]): return True
        return False


