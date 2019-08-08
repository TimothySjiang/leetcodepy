class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # write your code here
        start = matrix[0][0]
        end = matrix[-1][-1]

        while start <= end:
            mid = start + (end - start) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                start = mid + 1
            else:
                end = mid - 1
        if self.get_num_less_equal(matrix, start) >= k:
            return start
        return end

    def get_num_less_equal(self, matrix, mid):
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count