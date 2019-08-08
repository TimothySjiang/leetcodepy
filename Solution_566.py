class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums: return []
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0] * c for i in range(r)]
        for i in range(m * n):
            res[i // c][i % c] = nums[i // n][i % n]

        return res