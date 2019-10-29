class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        leftmin = [float('inf')] * len(nums)
        rightmax = [float('-inf')] * len(nums)
        for i in range(len(nums)):
            if i:
                leftmin[i] = min(leftmin[i - 1], nums[i])
            else:
                leftmin[0] = nums[0]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                rightmax[i] = nums[i]
            else:
                rightmax[i] = max(rightmax[i + 1], nums[i])

        for i in range(1, len(nums) - 1):
            if leftmin[i] < nums[i] < rightmax[i]:
                return True
        return False