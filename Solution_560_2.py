#classic wrong answer
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        p1, p2 = 0, 0
        total = 0

        while p1 < len(nums) and p2 < len(nums):
            while total <= k and p2 < len(nums):
                if total == k and p1 < p2:
                    count += 1
                total += nums[p2]
                p2 += 1

            while total >= k and p1 < len(nums):
                if total == k and p1 < p2:
                    count += 1
                total -= nums[p1]
                p1 += 1

        return count