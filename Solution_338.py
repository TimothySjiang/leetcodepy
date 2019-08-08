class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = 1 + dp[i - 2 ** int(math.log(i, 2))]

        return dp