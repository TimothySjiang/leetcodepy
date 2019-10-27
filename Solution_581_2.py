class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        newNums = sorted(nums)
        findStart = False
        for i in range(len(nums)):
            if nums[i] != newNums[i]:
                if not findStart:
                    findStart = True
                    start = i
                end = i
        if findStart:
            return end - start + 1
        else:
            return 0
