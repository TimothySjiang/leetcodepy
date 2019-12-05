class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.lis([x[1] for x in envelopes])

    def lis(self, nums):
        dp = []
        for num in nums:
            l = 0
            r = len(dp) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if dp[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == len(dp):
                dp.append(num)
            else:
                dp[l] = num
        return len(dp)