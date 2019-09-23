class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        result = []
        for num in nums:
            self.recursion(nums, result + [num], results)
        return results

    def recursion(self, nums, result, results):
        if len(nums) == len(result):
            results.append(result)
        for num in nums:
            if num not in result:
                self.recursion(nums, result + [num], results)
