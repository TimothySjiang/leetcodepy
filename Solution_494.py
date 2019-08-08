class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {0: 1}
        for x in nums:
            m = collections.defaultdict(int)
            for k in memo:
                v = memo[k]
                m[k + x] += v
                m[k - x] += v
            memo = m

        return memo[S]