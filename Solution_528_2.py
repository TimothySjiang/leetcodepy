class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w

    def pickIndex(self) -> int:
        num = random.uniform(0, 1) * self.w[-1]
        if num < self.w[0]:
            return 0
        l = 0
        r = len(self.w)
        while l < r:
            mid = l + (r - l) // 2
            if self.w[mid] < num:
                l = mid + 1
            else:
                r = mid
        return l

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()