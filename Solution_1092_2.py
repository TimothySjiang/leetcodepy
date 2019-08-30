class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        X = str1
        Y = str2
        m = len(X)
        n = len(Y)
        dp = [['']*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = X[:i]
        for j in range(1,n+1):
            dp[0][j] = Y[:j]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + X[i-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+X[i-1],dp[i][j-1]+Y[j-1],key = lambda x: len(x))
                dp[i-1][j-1] = ''
        return dp[-1][-1]