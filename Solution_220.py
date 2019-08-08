class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0: return False
        d = {}
        w = t + 1
        getID = lambda x, y: (x + 1) // y - 1 if x < 0 else x // y
        for i in range(len(nums)):
            m = getID(nums[i], w)
            if m in d.keys():
                return True

            if m - 1 in d.keys() and abs(nums[i] - d[m - 1]) < w:
                return True

            if m + 1 in d.keys() and abs(nums[i] - d[m + 1]) < w:
                return True

            d[m] = nums[i]

            if i >= k:
                d.pop(getID(nums[i - k], w))

        return False