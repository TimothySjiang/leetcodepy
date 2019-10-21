#MLE
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = [[] for i in range(len(s)+1)]
        dp[0].append('')
        for i in range(1,len(s)+1):
            res = []
            for j in range(i):
                if s[j:i] in wordSet:
                    for l in dp[j]:
                        res.append(l + ('' if l =='' else ' ') + s[j:i])
            dp[i] = res
        return dp[-1]