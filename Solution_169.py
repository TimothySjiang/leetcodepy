class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        level = len(nums)//2
        for val in c.keys():
            if c[val] > level:
                return val