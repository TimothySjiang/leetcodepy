class Solution:
    def distinctSubseqII(self, S: str) -> int:
        if not S: return 0
        modulo = 10**9 + 7
        dp = [0]*len(S)
        dp[0] = 1
        for i in range(len(S)):
            for j in range(i-1,-1,-1):
                dp[i] += dp[j]
                if S[i] == S[j]:
                    break
                if not j :
                    dp[i] += 1
        return sum(dp) % modulo