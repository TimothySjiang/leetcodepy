class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        # Write your code here.
        m, n = 0, 0
        for s in S:
            m += ord(s)-ord('0')
            n = min(m, n + ord('1') - ord(s))
        return n