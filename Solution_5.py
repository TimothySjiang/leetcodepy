class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPalindrome(s, p1, p2):
            while p1 > 0 and p2 < n - 1:
                if s[p1 - 1] != s[p2 + 1]:
                    return s[p1:p2 + 1]
                else:
                    p1 -= 1
                    p2 += 1

            return s[p1:p2 + 1]

        n = len(s)

        if n <= 1:
            return s
        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[-1]

        result = s[-1]

        for i in range(n - 2):
            if s[i] == s[i + 1]:
                sub = checkPalindrome(s, i, i + 1)
                result = max((len(sub), sub), (len(result), result))[1]
            if s[i] == s[i + 2]:
                sub = checkPalindrome(s, i, i + 2)
                result = max((len(sub), sub), (len(result), result))[1]

        if s[n - 2] == s[n - 1]:
            sub = checkPalindrome(s, n - 2, n - 1)
            result = max((len(sub), sub), (len(result), result))[1]

        return result