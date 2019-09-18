#Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        Max = max(nums)
        Min = min(nums)
        bucketSize = (Max - Min) // len(nums) + 1
        bucketNum = (Max - Min) // bucketSize + 1
        bucket = [[] for _ in range(bucketNum)]
        for n in nums:
            i = (n - Min) // bucketSize
            if not bucket[i]:
                bucket[i].append(n)
                bucket[i].append(n)
            elif n < bucket[i][0]:
                bucket[i][0] = n
            elif n > bucket[i][1]:
                bucket[i][1] = n

        gap = 0
        prev = 0
        for i in range(1, bucketNum):
            if bucket[i]:
                gap = max(gap, bucket[i][0] - bucket[prev][1])
                prev = i
        return gap