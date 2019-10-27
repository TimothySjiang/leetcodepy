class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l = len(nums)
        r = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1 if r > l else 0