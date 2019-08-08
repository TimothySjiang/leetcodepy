class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        result = []
        for k in c.keys():
            if c[k] > 1:
                result.append(k)

        return result