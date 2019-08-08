class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l  = 1
        r = max(piles)
        while l < r:
            m = l+(r-l)//2
            h = 0
            for p in piles:
                h += (p+m-1)//m
            if h <= H:
                r = m
            else:
                l = m+1
        return l