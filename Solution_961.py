class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        c = set()
        for i in A:
            if i in c:
                return i
            else:
                c.add(i)

