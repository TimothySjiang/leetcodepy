class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helpDC(start, end):
            if start >= end:
                return 0
            index = start
            for i in range(start, end):
                if heights[i] < heights[index]:
                    index = i
            return max(max(heights[index] * (end - start), helpDC(start, index)), helpDC(index + 1, end))

        return helpDC(0, len(heights))
