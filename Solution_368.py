class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n
        father = [-1] * n

        nums.sort()
        m, index = 0, -1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        father[i] = j

            if dp[i] >= m:
                m = dp[i]
                index = i

        result = []
        for i in range(m):
            result.append(nums[index])
            index = father[index]

        return result