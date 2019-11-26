class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        c = collections.Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return int(res)