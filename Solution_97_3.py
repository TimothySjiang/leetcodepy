#TLE
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        memo = [[0] * n for i in range(m)]
        return self.recursion(s1, 0, s2, 0, s3, 0, memo)

    def recursion(self, s1, index1, s2, index2, s3, index3, memo):
        if index1 == len(s1):
            return s2[index2:] == s3[index3:]
        if index2 == len(s2):
            return s1[index1:] == s3[index3:]
        if memo[index1][index2]:
            return True

        ans = False
        if s1[index1] == s3[index3]:
            ans = ans or self.recursion(s1, index1 + 1, s2, index2, s3, index3 + 1, memo)

        if s2[index2] == s3[index3]:
            ans = ans or self.recursion(s1, index1, s2, index2 + 1, s3, index3 + 1, memo)

        if ans: memo[index1][index2] = True

        return ans