class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for val in c.values():
            if val >= 2:
                return True

        return False