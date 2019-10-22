#TLE
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_i = float('inf')
        for j in range(len(nums)):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if nums[k] < nums[j] and min_i < nums[k]:
                    return True

        return False