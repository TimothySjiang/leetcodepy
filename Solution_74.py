class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = l + (r - l) // 2
            mi = m // len(matrix[0])
            mj = m % len(matrix[0])

            if matrix[mi][mj] == target:
                return True

            if matrix[mi][mj] > target:
                r = m - 1
            else:
                l = m + 1

        return False