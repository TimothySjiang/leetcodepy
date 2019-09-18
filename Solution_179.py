import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums.sort(key=functools.cmp_to_key(self.compare))
        return '0' if nums[0] == '0' else "".join(nums)

    def compare(self, a, b):
        if a + b < b + a:
            return 1
        elif a + b > b + a:
            return -1
        else:
            return 0