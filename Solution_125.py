class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        total = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "a", "b", "c", "d", "e", "f", "g", "h", "i",
                 "j", "k", "l", "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x", "y", "z"
                 }

        while i < j:
            while s[i] not in total and i < j:
                i = i + 1

            while s[j] not in total and i < j:
                j = j - 1

            if s[i] == s[j]:
                i = i + 1
                j = j - 1
                continue
            else:
                return False

        return True

