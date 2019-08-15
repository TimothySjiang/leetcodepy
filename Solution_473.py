class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        total = sum(nums)
        target = total // 4
        if target * 4 != total:
            return False
        nums.sort()
        k = 4
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        index = len(nums) - 1
        groups = [0] * k
        return self.dfs(nums, index, target, groups)

    def dfs(self, nums, index, target, groups):
        if index < 0: return True
        for i, group in enumerate(groups):
            if group + nums[index] <= target:
                groups[i] += nums[index]
                if self.dfs(nums, index - 1, target, groups): return True
                groups[i] -= nums[index]
            if not group: return False
        return False