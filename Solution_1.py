class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i,num in enumerate(nums):
            if num not in table:
                table[target-num] = i
            else:
                return [table[num],i]