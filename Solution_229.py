class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        n = len(nums) // 3
        result = []
        for x in c.keys():
            if c[x] > n:
                result.append(x)

        return result