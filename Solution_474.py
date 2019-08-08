class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for s in strs:
            zero = 0
            one = 0
            for ch in s:
                if ch == "1":
                    one += 1
                else:
                    zero += 1
            for i in range(n,one - 1,-1):
                for j in range(m,zero - 1,-1):
                    if dp[i - one][j - zero] + 1 > dp[i][j]:
                        dp[i][j] = dp[i - one][j - zero] + 1
        return dp[-1][-1]