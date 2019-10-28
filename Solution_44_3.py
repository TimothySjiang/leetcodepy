#TLE
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return True
        if not p and s: return False
        p = self.removeDuplicateStar(p)
        dp = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        dp[0][0] = True
        if p[0] == '*':
            for j in range(len(s) + 1):
                dp[1][j] = True

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = any([dp[i - 1][k] for k in range(j + 1)])
        return dp[-1][-1]

    def removeDuplicateStar(self, p):
        res = [p[0]]
        for i in range(1, len(p)):
            if p[i] != '*' or res[-1] != '*':
                res.append(p[i])
        return ''.join(res)