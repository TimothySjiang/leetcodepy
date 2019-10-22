class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        m = [0] * len(nums)
        m[0] = nums[0]
        for i in range(1, len(nums)):
            m[i] = min(m[i - 1], nums[i])
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > m[j]:
                while stack and stack[-1] <= m[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False