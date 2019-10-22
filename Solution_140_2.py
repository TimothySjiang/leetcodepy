class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {len(s): ['']}
        return self.sentences(s, 0, wordSet, memo)

    def sentences(self, s, i, wordSet, memo):
        if i not in memo:
            memo[i] = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet:
                    for tail in self.sentences(s, j, wordSet, memo):
                        memo[i].append(s[i:j] + (tail if tail == '' else ' ' + tail))
        return memo[i]