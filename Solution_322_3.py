class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        self.result = float('inf')
        self.dfs(coins, amount, len(coins) - 1, 0)
        return self.result if self.result < float('inf') else -1

    def dfs(self, coins, amount, index, count):
        if amount < 0:
            return
        if count > self.result:
            return
        if amount == 0:
            self.result = count
            return
        for i in range(index, -1, -1):
            self.dfs(coins, amount - coins[i], i, count + 1)
