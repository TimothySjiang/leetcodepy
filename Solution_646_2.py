class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = float('-inf'), 0
        for pair in sorted(pairs, key=lambda x: x[1]):
            if cur < pair[0]:
                cur = pair[1]
                res += 1
        return res
