class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # write your code here
        if not dungeon: return
        r, c = len(dungeon), len(dungeon[0])
        dp = [0 for _ in range(c)]
        dp[-1] = max(1, 1-dungeon[-1][-1])
        for i in range(c-2, -1, -1):
            dp[i] = max(1, dp[i+1]-dungeon[-1][i])
        for i in range(r-2, -1, -1):
            dp[-1] = max(1, dp[-1]-dungeon[i][-1])
            for j in range(c-2, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j+1])-dungeon[i][j])
        return dp[0]