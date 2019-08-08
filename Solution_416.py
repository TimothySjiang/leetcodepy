class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if target * 2 != total:
            return False

        nums.sort()
        if nums[-1] > target:
            return False

        return self.search(nums, [0] * 2, target)

    def search(self, nums, groups, target):
        if not nums: return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if self.search(nums, groups, target): return True
                groups[i] -= v
            if not group: break
        nums.append(v)
        return False