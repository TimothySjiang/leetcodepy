class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        result = s[-1]
        for i in range(n):
            p1 = i
            p2 = i
            while 0 < p1 and p2 < n - 1:
                if s[p1 - 1] == s[p2 + 1]:
                    p1 -= 1
                    p2 += 1
                else:
                    break
            sub = s[p1:p2 + 1]

            result = max((len(result), result), (len(sub), sub))[1]

            p1 = i
            p2 = i + 1
            if p1 < n - 1 and s[p1] == s[p2]:
                while 0 < p1 and p2 < n - 1:
                    if s[p1 - 1] == s[p2 + 1]:
                        p1 -= 1
                        p2 += 1
                    else:
                        break

                sub = s[p1:p2 + 1]

                result = max((len(result), result), (len(sub), sub))[1]

        return result
