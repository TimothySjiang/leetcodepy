class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = [0]
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.sum.append(total)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)