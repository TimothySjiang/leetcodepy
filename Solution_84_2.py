class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        index = heights.index(min(heights))
        area = heights[index]*len(heights)
        return max(max(area,self.largestRectangleArea(heights[:index])),self.largestRectangleArea(heights[index+1:]))