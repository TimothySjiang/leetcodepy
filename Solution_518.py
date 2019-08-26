class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        return self.recursion(amount, coins, current=0, index=0)

    def recursion(self, amount, coins, current, index):
        if current == amount:
            return 1
        res = 0
        for i in range(index, len(coins)):
            if current + coins[i] <= amount:
                res += self.recursion(amount, coins, current + coins[i], i)
        return res