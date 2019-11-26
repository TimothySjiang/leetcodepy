#TLE
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        s, res = set(), 0
        for num in A:
            if num not in s:
                s.add(num)
            else:
                count = 0
                while num in s:
                    num += 1
                    count += 1
                s.add(num)
                res += count
        return res