class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = collections.Counter(S)
        res = 0
        for j in J:
            res += c[j]
        return res
