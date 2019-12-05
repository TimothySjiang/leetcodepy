#TLE
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i):
                child = envelopes[j]
                parent = envelopes[i]
                if parent[0] > child[0] and parent[1] > child[1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)