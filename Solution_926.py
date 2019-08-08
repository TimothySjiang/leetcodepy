class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        l = [ord(S[0]) - ord('0')]
        for i in range(1, n):
            l.append(l[i - 1] + ord(S[i]) - ord('0'))

        r = [ord('1') - ord(S[-1])]
        for i in range(1, n):
            r.append(r[i - 1] + ord('1') - ord(S[-i - 1]))

        ans = min(r[-1], l[-1])
        for i in range(1, n - 1):
            ans = min(ans, l[i - 1] + r[-i - 2])

        return ans