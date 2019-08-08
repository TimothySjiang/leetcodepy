class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        a = [0 for i in range(len(matrix[0]))]
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == '1':
                    a[j] += 1
                else:
                    a[j] = 0
            maxArea = max(maxArea, self.largestRectangleArea(a))
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        index = heights.index(min(heights))
        area = heights[index] * len(heights)
        return max(max(area, self.largestRectangleArea(heights[:index])),
                   self.largestRectangleArea(heights[index + 1:]))