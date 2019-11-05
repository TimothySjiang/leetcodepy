class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = 1
        r = sum(weights) + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.valid(weights, D, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def valid(self, weight, days, capacity):
        total = 0
        for w in weight:
            if w > capacity: return False
            total += w
            if total > capacity:
                days -= 1
                total = w
        if total:
            days -= 1

        return True if days >= 0 else False