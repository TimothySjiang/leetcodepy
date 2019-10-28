#TLE
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        minHeight = float('inf')
        minIndex = float('inf')
        for i,height in enumerate(heights):
            if height < minHeight:
                minIndex = i
                minHeight = height
        area = len(heights) * minHeight
        left = self.largestRectangleArea(heights[:minIndex])
        right = self.largestRectangleArea(heights[minIndex+1:])
        area = max([area,left,right])
        return area