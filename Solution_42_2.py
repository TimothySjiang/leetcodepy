#ans
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        for curr in range(len(height)):
            while stack and height[curr] > height[stack[-1]]:
                pos = stack.pop()
                if not stack: break
                length = curr - stack[-1] - 1
                H = min(height[curr], height[stack[-1]]) - height[pos]
                res += length * H
            stack.append(curr)
        return res
