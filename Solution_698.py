class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k
        if target * k != total:
            return False
        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return self.search([0] * k, nums, target)

    def search(self, groups, nums, target):
        if not nums: return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if self.search(groups, nums, target): return True
                groups[i] -= v
            if not group: break
        nums.append(v)
        return False