class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.dfs(candidates, target, index=0, path=[])
        return self.res

    def dfs(self, nums, target, index, path):
        if target == 0:
            self.res.append(path)
        for i in range(index, len(nums)):
            if target - nums[i] < 0:
                break
            self.dfs(nums, target - nums[i], i, path + [nums[i]])