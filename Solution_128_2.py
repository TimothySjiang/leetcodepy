class Solution:
    def longestConsecutive(self, num):
        num = sorted(list(set(num)))
        p1, p2, res = 0, 0, 0
        while p1 < len(num):
            while p2 < len(num) - 1 and num[p2] + 1 == num[p2 + 1]:
                p2 += 1
            res = max(res, p2 - p1 + 1)
            p2 += 1
            p1 = p2
        return res
