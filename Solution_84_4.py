class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        res = float('-inf')
        stack = []
        for i, h in enumerate(heights):
            if not stack or heights[stack[-1]] < h:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    if not stack:
                        length = i
                    else:
                        length = i - stack[-1] - 1
                    res = max(res, height * length)
                stack.append(i)

        while stack:
            height = heights[stack.pop()]
            if not stack:
                length = len(heights)
            else:
                length = len(heights) - stack[-1] - 1
            res = max(res, height * length)

        return res