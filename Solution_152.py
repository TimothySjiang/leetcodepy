class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return None
        res = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            if num > 0:
                curr_max = max(num, prev_max * num)
                curr_min = min(num, prev_min * num)
            else:
                curr_max = max(num, prev_min * num)
                curr_min = min(num, prev_max * num)

            res = max(res, curr_max)
            prev_max, prev_min = curr_max, curr_min

        return res