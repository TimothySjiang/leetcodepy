class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            ans = max(ans, self.closestHeater(house, heaters))
        return ans

    def closestHeater(self, house, heaters):
        l = 0
        r = len(heaters) - 1
        while l + 1 < r:
            m = l + (r - l) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] > house:
                r = m
            else:
                l = m
        return min(abs(house - heaters[l]), abs(heaters[r] - house))