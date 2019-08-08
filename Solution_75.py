class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = collections.Counter(nums)
        start = 0
        for i in sorted(c):
            nums[start:(start+c[i])] = [i]*c[i]
            start += c[i]