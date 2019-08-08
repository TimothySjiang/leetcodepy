class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i]:
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
                else:
                    break
        return dp[-1]