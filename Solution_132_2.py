#TLE
class Solution:
    def minCut(self, s: str) -> int:
        if not s: return []
        results = []
        dp = self.isPalindrome(s)
        self.recursion(s,dp, 0, 0, results)
        return min(results)-1

    def recursion(self, s, dp, pos, result, results):
        if pos == len(s):
            results.append(result)
            return
        for i in range(pos, len(s)):
            if dp[pos][i]:
                self.recursion(s, dp, i + 1, result + 1, results)

    def isPalindrome(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if(s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1] == 1)):
                    dp[j][i] = 1
        return dp