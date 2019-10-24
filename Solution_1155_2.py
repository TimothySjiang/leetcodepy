class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [0] * (target + 1)
        for i in range(1,min(f,target)+1):
            dp[i] = 1
        for i in range(1,d):
            newdp = [0] * (target + 1)
            for j in range(i+1,target+1):
                for num in range(1,f+1):
                    if j - num > 0:
                        newdp[j] += dp[j-num]
            dp = newdp
        return dp[-1] % (modulo)