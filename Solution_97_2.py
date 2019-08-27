class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.recursion(s1, 0, s2, 0, '', s3, set())

    def recursion(self, s1, index1, s2, index2, res, s3, trueset):
        if res == s3 and index1 == len(s1) and index2 == len(s2):
            return True
        if (index1, index2) in trueset:
            return true

        ans = False
        if index1 < len(s1):
            if s1[index1] == s3[len(res)]:
                ans = ans or self.recursion(s1, index1 + 1, s2, index2, res + s1[index1], s3, trueset)
        if index2 < len(s2):
            if s2[index2] == s3[len(res)]:
                ans = ans or self.recursion(s1, index1, s2, index2 + 1, res + s2[index2], s3, trueset)

        if ans:
            trueset.add((index1, index2))

        return ans